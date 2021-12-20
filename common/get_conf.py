"""
author：lulu
time:2020/12/23  17:06

"""
import os
from configparser import ConfigParser
from common.set_path import conf_path
class Conf(ConfigParser):
    def __init__(self,conf_name):
        """
        重写调用配置文件的方法
        :param conf_name:
        """
        super().__init__()
        self.read(conf_name,encoding="utf-8")

conf=Conf(os.path.join(conf_path,"conf.ini"))