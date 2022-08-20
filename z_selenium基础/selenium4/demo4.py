# author: 测试蔡坨坨
# datetime: 2022/8/20 21:11
# function: 模拟移动设备

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.execute_cdp_cmd(
    "Emulation.setDeviceMetricsOverride",
    {
        "width": 400,
        "height": 650,
        "mobile": True,
        "deviceScaleFactor": 100
    }
)

driver.get("https://www.caituotuo.top/")
driver.find_element(By.XPATH, '//*[@id="scroll-down"]/i').click()
time.sleep(3)
driver.quit()
