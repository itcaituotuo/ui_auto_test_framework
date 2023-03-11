# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨(caituotuo.top)
# 时间：2022/6/11 22:12
# 功能：

import time

import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.get_logger import GetLogger
from utils.get_yml_data import GetYmlData

yml = GetYmlData()
config = yml.get_yml_data("config/config.yml")
logger = GetLogger.get_logger()


@pytest.fixture(scope="function")
def access_web():
    """
    访问目标网址
    :return:
    """
    driver_type = config["driver_type"]
    url = config["login_url"]
    # 前置：打开浏览器
    try:
        driver = getattr(webdriver, driver_type)()
    except Exception as e:
        logger.error(e)
        driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    # 后置：关闭浏览器
    logger.info("----------所有用例执行完毕----------")
    time.sleep(3)
    driver.quit()


@pytest.fixture(scope="function")
def login(access_web):
    """
    登录系统
    :param access_web:
    :return:
    """
    data = yml.get_yml_data("data/login/r0.yml")
    LoginPage(access_web).login(data["username"], data["password"])
    yield access_web
    logger.info("----------单条用例执行完毕----------")
