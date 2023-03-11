# -*- coding:utf-8 -*-
# 作者：测试蔡坨坨(caituotuo.top)
# 时间：2023-3-12 03:05:13
# 功能：基类，对 Selenium api 进行二次封装

import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.calculate_time_difference import do_time
from utils.datetime_util import DateTimeUtil
from utils.get_logger import GetLogger
from utils.get_path_info import GetPathInfo
from utils.get_yml_data import GetYmlData


class BasePage(object):
    def __init__(self, driver):
        """
        实例化BasePage类时，最先执行的是__init__()方法，该方法的入参就是BasePage类的入参
        :param driver:
        """
        self.logger = GetLogger().get_logger()
        self.yml = GetYmlData()
        self.time = DateTimeUtil()

        # try:
        #     self.driver = webdriver.Chrome()
        # except Exception:
        #     raise NameError("No Chrome.")

        self.driver = driver

    def wait_ele_visible_(self, loc, doc, times=3, poll_frequency=0.5):
        """
        等待元素可见
        :param loc: 元素定位
        :param doc: 元素描述
        :param times: 最长等待时间
        :param poll_frequency: 轮询频率，调用 until 或 until_not方法中的间隔时间，默认为0.5秒
        :return:
        """
        try:
            @do_time
            def fun():
                WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(loc))

            self.logger.info("等待【{}】元素【{}】出现，耗时：{}豪秒".format(doc, loc, fun()))
        except Exception:
            self.logger.error("等待【{}】元素【{}】出现失败".format(doc, loc))
            self.save_screenshot_(doc)
            raise

    def find_element_(self, loc, doc):
        """
        查找元素
        :param loc: 元素定位 例如：login_icon_loc = (By.ID, "sb_form_q")
        :param doc:
        :return:
        """
        try:
            self.logger.info("开始查找【{}】元素【{}】".format(doc, loc))
            self.wait_ele_visible_(loc, doc)
            return self.driver.find_element(*loc)
        except Exception:
            self.logger.error("查找【{}】元素【{}】失败".format(doc, loc))
            self.save_screenshot_(doc)
            raise

    def _click_button(self, loc, doc, times=3, poll_frequency=0.5):
        """
        点击元素
        :param loc: 元素定位
        :param doc: 元素描述
        :param times: 最长等待时间
        :param poll_frequency: 轮询时间
        :return:
        """
        try:
            self.wait_ele_visible_(loc, doc, times, poll_frequency)
            self.find_element_(loc, doc).click()
            self.logger.info("点击【{}】元素【{}】成功".format(doc, loc))
        except Exception:
            self.logger.error("点击【{}】元素【{}】失败".format(doc, loc))
            self.save_screenshot_(doc)
            raise

    def _send_keys(self, loc, text, doc, timeout=3, frequency=0.5, clear=True):
        """
        输入文本
        :param loc: 元素位置
        :param text: 要输入的文本内容
        :param doc: 元素描述
        :param timeout: 超时时间
        :param frequency: 频率
        :param clear: 是否清空文本框内容，默认为True
        :return:
        """
        try:
            self.logger.info("开始在【{}】元素中输入文本【{}】".format(doc, text))
            self.wait_ele_visible_(loc, doc, timeout, frequency)
            # time.sleep(10)
            if clear:
                self.find_element_(loc, doc).clear()
            self.find_element_(loc, doc).send_keys(text)
        except Exception:
            self.logger.exception("在【{}】元素中输入文本【{}】失败".format(doc, text))
            self.save_screenshot_(doc)
            raise

    def save_screenshot_(self, pic_name):
        """
        保存截图
        :param pic_name: 截图图片名称
        :return: None
        """
        try:
            # 图片命名：元素名称-年-月-日-时-分-秒.png
            screenshot_path = GetPathInfo().get_project_path() + r"/reports/screenshot"
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            file_name = screenshot_path + "/{}_{}.png".format(self.time.get_now_datetime_v2(), pic_name)
            self.driver.get_screenshot_as_file(file_name)
            self.logger.info("成功截图保存到{}".format(file_name))
        except Exception:
            self.logger.error("截图失败")
            raise

    def script(self, src):
        """
        执行JavaScript脚本
        :param src: JavaScript脚本
        """
        self.driver.execute_script(src)

    def _get_text(self, loc, doc):
        """
        获取文本信息
        :param loc:
        :param doc:
        :return: 文本信息
        """
        try:
            return self.find_element_(loc, doc).text
        except Exception:
            self.logger.error("获取文本失败")
            raise

    def _move_to_element(self, loc, doc):
        """
        鼠标悬浮
        :param loc: 元素定位
        :param doc: 描述
        :return:
        """
        try:
            self.logger.info("鼠标开始悬停在【{}】元素上".format(loc))
            ele = self.find_element_(loc, doc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception:
            self.logger.error("在元素【{}】进行悬浮失败！".format(loc))
            self.save_screenshot_(doc)
            raise
