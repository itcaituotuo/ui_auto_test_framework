# -*- coding:utf-8 -*-
# 作者：IT小学生蔡坨坨(caituotuo.top)
# 时间：2022/6/11 14:15
# 功能：UI自动化线性脚本

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sso.kuaidi100.com/sso/v2/authorize.do")
driver.maximize_window()
driver.find_element(By.ID, 'name').send_keys("***********")
driver.find_element(By.ID, 'password').send_keys("***********")
driver.find_element(By.ID, 'submit').click()
time.sleep(2)
text = driver.find_element(By.PARTIAL_LINK_TEXT, '首页').text
assert text == '首页'
driver.close()
