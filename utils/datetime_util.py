# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2022/5/16 16:39
# 功能：日期时间相关方法封装

import calendar
import time

from utils.get_logger import GetLogger


class DateTimeUtil:
    def __init__(self):
        self.logger = GetLogger().get_logger()

    def get_now_datetime(self):
        """
        格式化输出当前时间
        @return: 2022-06-01 14:29:08
        """
        try:
            now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.logger.error(e)

    def get_now_datetime_v2(self):
        """
        格式化输出当前时间
        @return: 2022-06-01-14-29-08
        """
        try:
            now_datetime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.logger.error(e)

    def get_gmtime(self):
        """
        获取当前时间戳
        @return: 时间戳，如：1654064948
        """
        try:
            return calendar.timegm(time.gmtime())
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    print(DateTimeUtil().get_now_datetime())
    print(DateTimeUtil().get_gmtime())
