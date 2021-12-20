"""
author：lulu
time:2020/12/17  20:02

"""

"""
设置每个目录的地址，用于其它文件调用

"""
import os

# 获取当前文件的绝对路径
abs_path = os.path.abspath(__file__)

# 获取根目录
base_path = os.path.dirname(os.path.dirname(abs_path))
# 获取日志和测试报告的目录
log_path = os.path.join(base_path, "log")
# 获取测试用例数据的目录
testcase_path = os.path.join(base_path, "testdata")
# 获取excel文件的目录
data_path = os.path.join(base_path, "data")
#获取配置文件的目录
conf_path=os.path.join(base_path,"conf")

