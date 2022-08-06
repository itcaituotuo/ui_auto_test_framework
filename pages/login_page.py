# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨(caituotuo.top)
# 时间：2022/6/11 19:13
# 功能：管理登录页面的所有元素 以及操作这些元素的所有方法

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    username_loc = (By.ID, 'name')
    password_loc = (By.ID, 'password')
    login_btn_loc = (By.ID, 'submit')
    warn_loc = (By.ID, 'warn')

    def login(self, username, password):
        self._send_keys(self.username_loc, username, "用户名输入框")
        self._send_keys(self.password_loc, password, "密码输入框")
        self._click_button(self.login_btn_loc, "登录按钮")

    def get_warn_text(self):
        return self._get_text(self.warn_loc, "提示信息")
