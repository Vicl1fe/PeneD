from utils.HttpUtil import HttpUtil
from utils.ColorUtil import ColorUtil
from utils.FileUtil import FileUtil
import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Update:
    def __init__(self,config):
        # 保存的目录
        self.save_dir = "result"
        self.config = config
        self.conf = config.config
        # head方法使用的头部，为了解决gzip编码导致的content-length与实际内容大小不符的问题。
        self.headHeader = {
            "User-Agent": HttpUtil.getRandUA(),
            "Accept-Encoding": "identity"
        }
        self.header = {
            "User-Agent": HttpUtil.getRandUA(),
        }

    def getFileSize(self,url,proxy=""):
        if proxy == "":
            try:
                rep = requests.get(url,headers=self.headHeader,verify=False)
            except requests.exceptions.ConnectionError as e:
                print(ColorUtil.Error(url + " Need Proxy"))
                return False
        else:
            rep = requests.get(url, headers=self.headHeader,proxies=proxy,verify=False)
        return rep.headers.get("Content-Length")


    def getProxy(self):
        if "proxy" in self.conf and self.conf["proxy"]["http"] != "" and self.conf["proxy"]["https"]!="":
            return self.conf["proxy"]
        else:
            print(ColorUtil.Warn("No Set Proxy！"))
            return ""

    def download(self,url,proxy=""):
        print(ColorUtil.Info("正在下载：%s"%url))

        if proxy == "":
            content_len = self.getFileSize(url)
            if content_len == False:
                return False
            rep = requests.get(url,headers=self.header,verify=False,stream=True)
        else:
            content_len = self.getFileSize(url,proxy)
            if content_len == False:
                return False

            rep = requests.get(url,headers=self.header,proxies=proxy,verify=False,stream=True)
        # 进度条

        temp_size = 0  # 已经下载文件大小
        chunk_size = 128  # 每次下载数据大小
        total_size = int(content_len)
        result = ""  # 存放最终数据。
        # 进度条

        result = self.processBar(rep,content_len)
        print()
        # 第一次去重
        temp = result.split(b"\n")
        # print(ColorUtil.Info("第一次去重前：%d"%len(temp)))
        temp = list(set(result.split(b"\n")))
        # print(ColorUtil.Info("第一次去重后：%d"%len(temp)))
        return temp

    def processBar(self,rep,content_len):
        temp_size = 0  # 已经下载文件大小
        chunk_size = 1024  # 每次下载数据大小
        total_size = int(content_len)
        result = b""  # 存放最终数据。
        # 进度条
        for chunk in rep.iter_content(chunk_size=chunk_size):
            if chunk:
                temp_size += len(chunk)
                try:
                    result += chunk
                except UnicodeDecodeError as e:
                    continue
                #############花哨的下载进度部分###############
                done = int(50 * temp_size / total_size)

                sys.stdout.write("\r[\033[1;34mINFO\033[0m] \033[1;32m[%s%s] %d%% %0.2fM\033[0m" % (
                '#' * done, ' ' * (50 - done), 100 * temp_size / total_size, temp_size / 1024 / 1024))
                sys.stdout.flush()
        return result
    def save(self,filename,content):

        if len(content) != 0:
            # 第二次去重
            print(ColorUtil.Info("去重前：%d" % len(content)))
            result = list(set(content))
            print(ColorUtil.Info("去重后：%d" % len(result)))
        # 保存文件
        path = FileUtil.getProjectPath() + FileUtil.getFileSep() + self.save_dir + FileUtil.getFileSep()
        absolute_path = path + filename + ".txt"

        if FileUtil.isFileExist(absolute_path) == False:
            FileUtil.createDirFile(absolute_path)
        f = open(absolute_path,"wb")

        f.write(b"\n".join(content))
        f.close()



    def update(self,type=""):
        proxy = self.getProxy()
        blacklist = self.conf["blacklist"]

        if type != "":
            if type in blacklist or type not in self.conf:
                print(ColorUtil.Error("No Type %s"%type))
                return
            result = []
            if len(self.conf[type]) == 0:
                print(ColorUtil.Error("Config(%s) is Empty！"%type))
                return
            print(ColorUtil.InfoBlue("=========Type：%s=========" % type))
            for url in self.conf[type]:
                # 本地文件
                if not url.startswith("http://") and not url.startswith("https://"):
                    if FileUtil.isFileExist(url):

                        print(ColorUtil.Info("正在读取：%s" % url))
                        result += open(url, "rb").readlines()
                    else:
                        print(ColorUtil.Error("No Path %s" % url))
                else: # 链接
                    temp = self.download(url, proxy)
                    if temp == False:
                        continue
                    result += temp
            self.save(type, result)
        else:

            for key in self.conf:
                result = []
                if len(self.conf[key]) == 0:
                    print(ColorUtil.Error("Config(%s) is Empty！"%key))
                    continue
                # 如果key在黑名单里，则继续下次循环。
                if key in blacklist:
                    continue
                print(ColorUtil.InfoBlue("=========Type：%s=========" % key))
                # 依次更新
                for url in self.conf[key]:
                    # 本地文件
                    if not url.startswith("http://") and not url.startswith("https://"):
                        if FileUtil.isFileExist(url):
                            print(ColorUtil.Info("正在读取：%s"%url))
                            result += open(url,"rb").readlines()
                        else:
                            print(ColorUtil.Error("No Path %s"%url))
                    else: # 链接
                        temp = self.download(url, proxy)
                        if temp == False:
                            continue
                        result += temp

                self.save(key, result)