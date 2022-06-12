# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨(caituotuo.top)
# 时间：2022/6/12 12:41
# 功能：个人信息页
import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class UserInfoPage(BasePage):
    def __init__(self, driver):
        super(UserInfoPage, self).__init__(driver)

    userinfo_icon_loc = (By.XPATH, '//div[3]/div[2]/div[1]/ul/li[2]/a')
    nic_loc = (By.ID, 'usernick')
    save_loc = (By.ID, 'saveProfile')
    tip_loc = (By.ID, 'errorTips')

    def edit_nic(self, nic):
        """
        修改昵称并保存
        :return:
        """
        self._click_button(self.userinfo_icon_loc, "用户信息tab")
        self._send_keys(self.nic_loc, nic, "昵称输入框")
        self._click_button(self.save_loc, "保存按钮")

    def get_tip(self):
        """
        获取提示信息
        :return: 提示信息
        """
        return self._get_text(self.tip_loc, "提示框")
