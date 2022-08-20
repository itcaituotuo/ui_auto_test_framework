# author: 测试蔡坨坨
# datetime: 2022/8/20 19:19
# function: 元素定位

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 不推荐
# driver.find_element_by_id("kw").send_keys("测试蔡坨坨")
# driver.find_element_by_id("su").click()

# 推荐
driver.find_element(By.ID, "kw").send_keys("测试蔡坨坨")
driver.find_element(By.ID, "su").click()
time.sleep(3)

driver.quit()
