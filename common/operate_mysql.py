"""
author：lulu
time:2020/12/27  10:20

"""
import pymysql
from common.get_conf import conf


class Operate_DB():

    def __init__(self):
        self.con = pymysql.connect(host=conf.get("mysql", "address"), port=eval(conf.get("mysql", "port")),
                                   user=conf.get("mysql", "user"),
                                   password=conf.get("mysql", "pwd"), charset="utf8",cursorclass=pymysql.cursors.DictCursor)

    def search_datas(self,sql):
        """
        查询到的所有数据
        :param sql: 传入sql
        :return:
        """
        with self.con as cur:
            cur.execute(sql)
        cur.close()
        return cur.fetchall()

    def search_data(self,sql):
        """
        查询到的第一条数据
        :param sql: 传入sql
        :return:
        """
        cur=self.con.cursor()
        cur.execute(sql)
        cur.close()
        return cur.fetchone()

    def data_count(self,sql):
        """
        返回sql查询的数据条数
        :param sql: 传入sql
        :return:
        """
        cur=self.con.cursor()
        count=cur.execute(sql)
        cur.close()
        return count
    def __del__(self):
        """
        对象使用完后自动调用
        :return:
        """
        self.con.close()


# if __name__ == '__main__':
#     a = Operate_DB()
#     print(a.data_count("SELECT * FROM ARCHIVE.user "))
