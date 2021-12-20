"""
author：lulu
time:2021/3/12  9:19

"""
import random
from common.operate_mysql import Operate_DB

# 生成随机数
def random_num():
    random_num=random.randint(1, 999999999)
    return random_num

# def decode(data,desc,salt):
#     """
#     通过数据库select语句解密数据：先aes加密再base64加密的数据
#     :param data: 要解密的数据
#     :param desc: 设置字典的键便于获取值
#     :param key: 解密的盐值
#     :return:
#     """
#     decode_data = str(Operate_DB().search_data(
#         f'select AES_DECRYPT(from_base64("{data}"),"{salt}") as {desc}')[
#                                           f"{desc}"], encoding="utf-8")
#     return decode_data
#
#
# def encode(data,desc,salt):
#     """
#     通过数据库select语句加密数据：先aes加密再base64加密的数据
#     :param data: 要加密的数据
#     :param desc: 设置字典的键便于获取值
#     :param key: 加密的盐值
#     :return:
#     """
#     encode_data = Operate_DB().search_data(
#         f'select to_base64(AES_ENCRYPT("{data}","{salt}")) as {desc}')[
#                                           f"{desc}"]
#     return encode_data





