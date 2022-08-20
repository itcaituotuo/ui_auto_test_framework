# author: 测试蔡坨坨
# datetime: 2022/8/20 19:19
# function: 相对位置定位

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name

driver = webdriver.Chrome()

driver.get("https://www.caituotuo.top/")

driver.find_element(By.XPATH, '//*[@id="scroll-down"]/i').click()
time.sleep(2)
# 文章标题
article_title = driver.find_element(By.CLASS_NAME, "article-title")
# 获取文章标题左侧的图片
elements = driver.find_elements(with_tag_name('img').to_left_of(article_title))
for e in elements:
    print(e.get_attribute('src'))

driver.quit()
