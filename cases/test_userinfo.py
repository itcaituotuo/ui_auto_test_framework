# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨(caituotuo.top)
# 时间：2022/6/12 13:54
# 功能：用户资料 相关测试用例

import allure
import pytest

from pages.userinfo_page import UserInfoPage


class TestUserInfo:
    @allure.title("修改昵称")
    @pytest.mark.usefixtures("login")
    def test_1(self, login):
        obj = UserInfoPage(login)
        obj.edit_nic("IT小学生蔡坨坨")
        expect = obj.get_tip()
        assert expect == "修改成功"
