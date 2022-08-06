# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨
# 时间：2022/3/16 20:10
# 功能：日志模块封装

import logging
import os
import time
from logging import handlers

from utils.get_path_info import GetPathInfo


class GetLogger(object):
    """ 日志封装类 """

    @classmethod
    def get_logger(cls):
        log = logging.getLogger(__name__)  # 不会打印 HTTP General 信息
        # log = logging.getLogger()
        level_relations = {
            'NOTSET': logging.NOTSET,
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }  # 日志级别关系映射

        # 创建日志存放的目录
        project_path = GetPathInfo().get_project_path()  # get_project_path()获取项目根目录
        logs_dir = project_path + "logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 日志文件以日期命名
        log_file_name = '%s.log' % time.strftime("%Y-%m-%d", time.localtime())
        log_file_path = os.path.join(logs_dir, log_file_name)

        rotating_file_handler = handlers.TimedRotatingFileHandler(filename=log_file_path,
                                                                  when='D',  # 按天分隔，一天一个文件
                                                                  interval=30,
                                                                  encoding='utf-8')

        # 日志输出格式
        fmt = "%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(message)s"
        # fmt = "%(name)s %(asctime)s %(created)f %(relativeCreated)d %(msecs)d %(levelname)s %(levelno)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(process)d %(thread)d %(threadName)s %(message)s"
        formatter = logging.Formatter(fmt)
        rotating_file_handler.setFormatter(formatter)

        # 加上判断，避免重复打印日志
        if not log.handlers:
            # 控制台输出
            console = logging.StreamHandler()
            console.setLevel(level_relations["NOTSET"])
            console.setFormatter(formatter)
            # 写入日志文件
            log.addHandler(rotating_file_handler)
            log.addHandler(console)
            log.setLevel(level_relations['DEBUG'])
        return log


if __name__ == '__main__':
    logger = GetLogger().get_logger()
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')
    # print(datetime.datetime.now())
    # print(time.time())
