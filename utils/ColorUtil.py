

class ColorUtil:

    @staticmethod
    def Info(stat):
        return "[\033[1;34mINFO\033[0m] \033[1;32m{}\033[0m".format(stat)

    @staticmethod
    def Warn(stat):
        return "[\033[1;33mWARN\033[0m] \033[1;33m{}\033[0m".format(stat)

    @staticmethod
    def Error(stat):
        return "[\033[1;31mERROR\033[0m] \033[1;31m{}\033[0m".format(stat)

    @staticmethod
    def InfoBlue(stat):
        return "[\033[1;34mINFO\033[0m] \033[1;34m{}\033[0m".format(stat)
