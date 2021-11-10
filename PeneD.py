import sys
import os
from config import Config
from lib.Function import *
from lib.Update import Update

os.system('') #命令行颜色问题
filename = os.path.basename(__file__)

class Dict:
    def __init__(self):
        self.config = Config()

    def main(self):
        if len(sys.argv) == 1:
            self.help()
            sys.exit()

        self.config.init()
        # 获取选项
        if sys.argv[1].lower() == "add":
            if len(sys.argv) == 3:
                Function.add(self.config,sys.argv[2])
            else:
                self.help()
        elif sys.argv[1].lower() == "update":
            if len(sys.argv) == 3:
                Update(self.config).update(sys.argv[2])
            else:
                Update(self.config).update()
        elif sys.argv[1].lower() == "proxy":
            if len(sys.argv) == 3:
                Function.setProxy(self.config,sys.argv[2])
            else:
                self.help()
        elif sys.argv[1].lower() == "show":
            Function.show(self.config.config)
        elif sys.argv[1].lower() == "delete":
            if len(sys.argv) == 3:
                Function.delete(self.config,sys.argv[2])
            else:
                self.help()

        else:
            self.help()
            sys.exit()


    def help(self):

        print("Usage：\n\tpython " + filename + " Option [arguments]")

        print("Option：")
        print("\t{} 	{:<10}".format("add","添加Url/本地绝对路径名到配置文件中"))
        print("\t{}  {:<10}".format("update","更新字典"))
        print("\t{}   {:<10}".format("proxy","设置代理"))
        print("\t{}    {:<10}".format("show","查看配置信息"))
        print("\t{}  {:<10}".format("delete", "删除某条配置信息"))

        print("Example：")
        print("\tpython " + filename + " add php:http://xxx.com/php.txt")
        print("\tpython " + filename + " add php:E:\dict\php.txt")
        print("\tpython " + filename + " proxy http://127.0.0.1:1081")
        print("\tpython " + filename + " proxy socks5://127.0.0.1:1080")
        print("\tpython " + filename + " proxy \"\" // 删除代理")
        print("\tpython " + filename + " show")
        print("\tpython " + filename + " update")
        print("\tpython " + filename + " update php")
        print("\tpython " + filename + " delete php:http://xxx.com/php.txt")

        print("\nAuthor Vicl1fe")


if __name__ == '__main__':
    Dict().main()