# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2022/3/12 20:50
# 功能：获取路径信息
import os


class GetPathInfo:
    def get_project_path(self):
        """ 获取项目根路径 """
        return os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\"


if __name__ == '__main__':
    print(GetPathInfo().get_project_path())
