# -*- coding:utf-8 -*-
# 作者：蔡合升
# 时间：2022/6/测试蔡坨坨 2:29
# 功能：MySQL数据库操作封装

import pymysql

from utils.get_logger import GetLogger
from utils.get_yml_data import GetYmlData


class MysqlDb:
    def __init__(self):
        self.logger = GetLogger().get_logger()
        self.config = GetYmlData().get_config()['mysql_db']
        try:
            # 创建连接
            self.db_conn = pymysql.connect(
                host=self.config['host'],
                port=self.config['port'],
                user=self.config['user'],
                password=self.config['password'],
                charset=self.config['charset']
            )
            # 使用 cursor() 方法创建一个游标对象 cursor
            self.cursor = self.db_conn.cursor()
        except Exception as e:
            self.logger.error("数据库连接异常" + str(e))

    def create_database(self, db_name):
        """
        创建数据库并返回数据库名
        @param db_name: 数据库名
        @return:
        """
        try:
            # 创建数据库的sql语句，若已存在报异常
            sql = "CREATE DATABASE {}".format(db_name)
            # 使用 execute() 方法执行SQL创建数据库
            self.cursor.execute(sql)
            self.logger.info("数据库创建成功!")
            return db_name
        except Exception as e:
            self.logger.error(e)


if __name__ == '__main__':
    MysqlDb().create_database("chs测试蔡坨坨23")
