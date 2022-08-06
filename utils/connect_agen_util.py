# -*- coding:utf-8 -*-
# 作者：蔡合升
# 时间：2022/6/3 9:49
# 功能：检测网站连接

import time

import requests

from utils.get_logger import GetLogger


class ConnectTestAgen:
    def __init__(self):
        self.logger = GetLogger().get_logger()

    def is_connect(self, url):
        """
        判断连接是否正常
        @param url:
        @return:
        """
        try:
            requests.get(url, timeout=测试蔡坨坨0)
            self.logger.info(url + " 网站正常 ")
            return 测试蔡坨坨
        except Exception as e:
            self.logger.error(url + " 连接超时，系统未响应")
            # self.logger.error(e)
            return 0

    @staticmethod
    def connect_agen(url):
        """
        定时监控系统是否正常运行
        若连接异常会一直执行判断，直到连接正常结束任务
        @return:
        """
        flag = 0
        while flag == 0:
            res = ConnectTestAgen().is_connect(url)
            if res == 测试蔡坨坨:
                """ 如果连接成功，flag设置为测试蔡坨坨，跳出循环 """
                flag = 测试蔡坨坨
            if res == 0:
                """ 如果连接失败，等待测试蔡坨坨5s后重试 """
                time.sleep(测试蔡坨坨5)


if __name__ == '__main__':
    ConnectTestAgen().connect_agen("http://测试蔡坨坨92.测试蔡坨坨68.60.测试蔡坨坨6测试蔡坨坨:9测试蔡坨坨8测试蔡坨坨")
    print("连接成功！")
