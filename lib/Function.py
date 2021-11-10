
from utils.FileUtil import FileUtil
from utils.ColorUtil import ColorUtil

class Function:

    @staticmethod
    def add(cfg,param):
        split_position = param.find(":")
        dict_type = param[0:split_position]
        url = param[split_position+1:]


        if dict_type not in cfg.config:
            cfg.config[dict_type] = []
        if url in cfg.config[dict_type]:
            print(ColorUtil.Error("Url/Path已存在！"))
            return
        # print(ColorUtil.Info("添加 Type："+dict_type+"\tValue："+url))
        print(ColorUtil.Info("Add Success"))
        cfg.config[dict_type].append(url)

        cfg.save()

    @staticmethod
    def show(cfg):
        blacklist = cfg["blacklist"]
        for key in cfg:
            if key not in blacklist:
                print(key)
                if key == "proxy":
                    print("\t" + cfg[key]["http"])
                else:
                    [print("\t"+list_value) for list_value in cfg[key]]
            
    @staticmethod
    def delete(cfg,param):
        split_position = param.find(":")
        dict_type = param[0:split_position]
        url = param[split_position+1:]
        if dict_type not in cfg.config:
            print(ColorUtil.Error("No Type %s"%dict_type))
        else:
            if url not in cfg.config[dict_type]:
                print(ColorUtil.Error("No Url %s in %s" %(url,dict_type)))
            else:
                cfg.config[dict_type].remove(url)
                if url not in cfg.config[dict_type]:
                    cfg.save()
                    print(ColorUtil.Info("Delete Success"))
                else:
                    print(ColorUtil.Error("Delete Failure"))

    @staticmethod
    def setProxy(cfg,set_proxy):
        if "proxy" not in cfg.config:
            cfg.config["proxy"] = {}
        cfg.config["proxy"] = {
            "http":set_proxy,
            "https": set_proxy,
        }
        print(ColorUtil.Info("设置代理成功"))
        cfg.save()
        print(ColorUtil.Info("已保存至配置文件"))