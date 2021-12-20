"""
author：lulu
time:2020/12/17  10:44

"""

import json, os, unittest, requests
from common.set_path import data_path
from jsonpath import jsonpath
from common.get_excel import RW_excel
from unittestreport import ddt, list_data
from common.set_log import log
from common.get_conf import conf
from common.get_token import Login


@ddt
class Test_SearchCar(unittest.TestCase):
    '''
    车辆系统查询接口
    '''

    # 读取hy_inter.xlsx文件内容,保存格式[{},{},{}]
    excel = RW_excel(filename=os.path.join(data_path, "hycar_inter.xlsx"), sheetname="search")
    data = excel.r_excel()
    base_url = conf.get("env", "hy_manager_url")

    @classmethod
    def setUpClass(cls) -> None:
        # 执行用例之前调用一次登录获取token
        cls.token = Login().get_token()

    @list_data(data)
    def test_searchcar(self, params):
        expect = json.loads(params["expected"])
        url = self.base_url + params["url"]
        data = eval(params["data"].replace("${token}$", self.token).replace("${vehicleNumber}$", "粤B1AB33").replace(
            "${vehiclePlateColorCode}$", "5"))
        method = params["method"].lower()
        respon = requests.request(method=method, url=url, json=data)
        log.info("调用（{}）接口".format(params["desc"]))
        # row = params["case_id"] + 1
        respon_content = respon.json()
        print(respon_content)
        print("预期结果:", expect)
        print("实际结果：", respon_content)
        try:
            self.assertEqual(expect["code"], jsonpath(respon_content, "$.code")[0])
            log.info("判断code期望值是否等于返回值")
        except AssertionError as e:
            log.error("用例【{}】执行失败".format(params["desc"]))
            log.exception(e)
            # 数据回写到excel
            # self.excel.w_excel(row=row, cell=9, value="失败")
            # self.excel.w_excel(row=row, cell=8, value=respon.content.decode("utf-8"))
            raise e
        except Exception as e:
            log.exception(e)
            raise e
        else:
            log.info("用例【{}】执行成功".format(params["desc"]))
            # 数据回写到excel
            # self.excel.w_excel(row=row, cell=9, value="成功")
            # self.excel.w_excel(row=row, cell=8, value=respon.content.decode("utf-8"))
