import os
import time
import platform

class FileUtil:

    @staticmethod
    def getOperatingSystemType():
        return platform.system()

    # 获取文件分割符
    @staticmethod
    def getFileSep():
        return os.sep

    # 返回项目根目录
    @staticmethod
    def getProjectPath():
        return os.path.dirname(os.path.dirname(__file__))

    # 判断文件存在
    @staticmethod
    def isFileExist(path):
        return os.path.exists(path)

    # 创建新文件
    @staticmethod
    def createFile(path):
        open(path,"w",encoding="utf-8").close()

    # 创建文件及目录
    def createDirFile(path):
        if not FileUtil.isFileExist(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
            FileUtil.createFile(path)


    # 得到文件大小
    @staticmethod
    def getFileSize(path):
        return os.path.getsize(path)

    @staticmethod
    def currentTime():
        return time.time()
