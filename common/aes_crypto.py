"""
author：lulu
time:2021/3/13  9:16

"""
from Crypto.Cipher import AES  # PyCryptodome，
import base64


class AES_Crypto():
    '''
    AES-128-ECB模式加解密,加密只支持32位以下
    补位方式：pkcs7填充
    '''

    def __init__(self, key, text):
        self.text = text
        self.key = key

    # pkcs7填充，给传入的数据补充到16位或32位
    def add_to_digit(self):
        if len(self.text.encode()) <= 16:# 中文utf编码占3个位置，所以需要先转成encode再算长度
            self.digit = 16
        elif len(self.text.encode()) > 16 and len(self.text.encode()) <= 31:
            self.digit = 32
        num = self.digit - len(self.text.encode())
        if len(self.text.encode()) % self.digit != 0:
            for i in range(num):
                self.text += chr(num)
        return self.text

    def aes_encode(self):
        '''
        加密传入的数据:支持中文，字母，数字
        :return:加密后的字符串
        '''
        aes = AES.new(self.key.encode(encoding="utf-8"), AES.MODE_ECB)
        encode_content = aes.encrypt(self.add_to_digit().encode(encoding="utf-8"))
        encode_contentto_base64 = base64.b64encode(encode_content)
        return str(encode_contentto_base64, encoding="utf-8")

    def aes_decode(self):
        '''
        解密传入的密文
        :return: 解密后的字符串
        '''
        aes = AES.new(self.key.encode(encoding="utf-8"), AES.MODE_ECB)
        decode_content = aes.decrypt(base64.b64decode(self.text))
        last_byte = decode_content[len(decode_content) - 1:]  # 获取最后一个字符
        if ord(last_byte) in [i + 1 for i in range(15)]:
            return str(decode_content[:-ord(last_byte)], encoding="utf-8")  # 如果最后一个字符的十进制数在1-15之间，则需要过滤掉补位的ASCII字符
        else:
            return str(decode_content, encoding="utf-8")  # 如果最后一个字符的十进制数为ASCII码，说明没有进行补位，不需要过滤


# if __name__ == '__main__':
#     a = AES_Crypto("7f467bed76056a22", "哈哈哈哈")
#     c = a.aes_encode()
#     print(c)
#     b = AES_Crypto("7f467bed76056a22", "DwRtsqO7G5TJra0+kgUuiQ==")
#     d = b.aes_decode()
#     print(d, type(d))
#     assert "哈哈哈哈" == d
