# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨
# 时间：2021/8/24 0:19
# 功能：批量执行测试用例，并生成Allure测试报告

import os

import pytest


class TestRun:
    def test_run_default(self):
        # 测试用例
        case = ["cases/test_login.py", "cases/test_userinfo.py"]

        # allure-json存放路径
        allure_json = "reports/"
        if not os.path.exists(allure_json):
            os.makedirs(allure_json)

        # 定义PyTest运行参数
        param_list = ["-s", "-v", "-rA", "--alluredir={}".format(allure_json)]
        param_list.extend(case)

        # 执行用例，并生成测试报告
        pytest.main(param_list)
        os.system("allure generate {} --clean".format(allure_json))


if __name__ == '__main__':
    TestRun().test_run_default()
