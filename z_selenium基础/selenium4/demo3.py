# author: 测试蔡坨坨
# datetime: 2022/8/20 23:37:32
# function: 打开新的标签页或窗口

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.caituotuo.top/")

# 打开新的标签页，并切换进入
driver.switch_to.new_window("tab")
driver.get("https://www.cnblogs.com/caituotuo")
print(driver.title)

# 打开新的窗口，并切换进入
driver.switch_to.new_window("window")
driver.get("https://www.caituotuo.top/")
print(driver.title)

time.sleep(3)
driver.quit()
