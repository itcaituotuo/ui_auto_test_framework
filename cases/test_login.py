# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨(caituotuo.top)
# 时间：2022/6/11 21:02
# 功能：登录 测试用例

import allure
import pytest

from pages.login_page import LoginPage


class TestCaseLogin:

    @allure.title("登录——错误的用户名和密码")
    def test_0(self, access_web):
        obj = LoginPage(access_web)
        obj.login("123", "123")
        assert obj.get_warn_text() == "用户不存在或者密码错误"

    @allure.title("登录——正确的用户名和密码")
    @pytest.mark.usefixtures("login")
    def test_1(self, login):
        pass


if __name__ == '__main__':
    pytest.main()
