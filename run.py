"""
author：lulu
time:2020/12/17  15:50

"""
import unittest
from common.set_path import log_path, testcase_path
from unittestreport import TestRunner

loder = unittest.defaultTestLoader.discover(testcase_path)
runner = TestRunner(loder, tester="zll", desc="快运后台接口测试报告", report_dir=log_path)
runner.run()

#发送到邮箱
# runner.send_email(host="smtp.qq.com",port=465,user="2879292312@qq.com",password="vnonadshmfydddii",to_addrs="2879292312@qq.com",is_file=True)
#发送到钉钉
# runner.dingtalk_notice(url="https://oapi.dingtalk.com/robot/send?access_token=bce9c341795d31c0b103f028be61f3bf71df0c6bdaa8d918f94a49130aa38f34",key="测试报告")
