"""
author：lulu
time:2020/12/17  17:43

"""
import logging
import os
from common.set_path import log_path

def setlog():
    """
    设置日志收集和输出的级别
    :return: 返回日志收集器log
    """
    log = logging.getLogger("接口日志")
    log.setLevel("INFO")

    # 输出日志到文件
    file_log = logging.FileHandler(filename=os.path.join(log_path,"car_log.log"), encoding="utf-8")
    file_log.setLevel("INFO")
    log.addHandler(file_log)
    # 输出日志到控制台
    stream_log = logging.StreamHandler()
    stream_log.setLevel("INFO")
    log.addHandler(stream_log)

    fomater = logging.Formatter(
        "%(asctime)s %(filename)s line:%(lineno)d %(levelname)s: %(message)s")
    file_log.setFormatter(fomater)
    stream_log.setFormatter(fomater)

    return log

log=setlog()
