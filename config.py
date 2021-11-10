from utils.FileUtil import FileUtil
from utils.ColorUtil import ColorUtil
import json

class Config:
    def __init__(self):
        self.config_filename = "config.json"
        self.file_encode = "utf-8"
        self.project_path = FileUtil.getProjectPath()
        self.file_sep =  FileUtil.getFileSep()
        self.init_data = {
            "php":[

            ],
            "asp":[

            ],
            "jsp":[

            ],
            "blacklist":[
                "blacklist"
            ]
        }
        self.config = {}

    def init(self):
        config_allpath = self.project_path + self.file_sep + self.config_filename

        # 配置文件不存在则创建
        if FileUtil.isFileExist(config_allpath) == False:
            FileUtil.createFile(config_allpath)
        f = open(config_allpath,"r+",encoding=self.file_encode)

        # 配置文件为空，则初始化配置文件,不为空则加载内容
        if FileUtil.getFileSize(config_allpath) == 0:
            print(ColorUtil.Info("配置文件初始化..."))
            f.write(json.dumps(self.init_data))
            self.config = self.init_data
            print(ColorUtil.Info("配置文件初始化完成！"))
        else:
            print(ColorUtil.Info("读取配置文件..."))
            content = [i for i in f.readlines()]
            self.config = json.loads("".join(content))
            print(ColorUtil.Info("读取配置文件完成！"))


    def save(self):
        config_allpath = self.project_path + self.file_sep + self.config_filename
        f = open(config_allpath, "w", encoding=self.file_encode)

        f.write(json.dumps(self.config))
        # print(ColorUtil.Info("配置文件保存成功..."))

