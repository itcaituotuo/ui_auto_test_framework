# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨(caituotuo.top)
# 时间：2022/6/11 21:02
# 功能：

import allure
import pytest

from pages.login_page import LoginPage
from utils.datetime_util import DateTimeUtil
from utils.get_logger import GetLogger


class TestCaseLogin:

    @allure.title("登录——正确的用户名和密码")
    @pytest.mark.usefixtures("login")
    def test_1(self, login):
        pass


if __name__ == '__main__':
    pytest.main()
