# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨(caituotuo.top)
# 时间：2022/6/11 22:54
# 功能：

import datetime
import time

from utils.get_logger import GetLogger


def do_time(func):
    """
    计算时间差 装饰器
    :param func:
    :return:
    """

    def fun():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        difference_time = (end_time - start_time).seconds * 1000
        return difference_time

    return fun


if __name__ == '__main__':
    @do_time
    def do():
        time.sleep(3)


    print(do())
