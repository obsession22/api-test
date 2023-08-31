#!/usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.read_yml import replace_py_yaml
from utils.read_yml import GetCaseYmal

import yaml


class Base:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    # 进入网页
    def load(self, url):
        # self.logger.info(f"加载网页: {url}")
        self.driver.get(url)

    # 元素查询
    def find_elements(self, types, locate):
        # self.logger.info("元素查询")
        element = WebDriverWait(self.driver, 10, 0.5).until(
            lambda x: x.find_element(types, locate), '没找到元素')
        return element

    # 窗口最大化
    def max_windows(self):
        # self.logger.info("窗口最大化")
        self.driver.maximize_window()

    # 元素等待
    def element_wait(self, types, locate):
        element = WebDriverWait(self.driver, 10, 0.5).until(
            lambda x: x.find_element(types, locate), '没有找到元素')
        return element

    # 点击
    def often_click(self, types, locate):
        self.find_elements(types, locate).click()

    # 设置值
    def send_key(self, types, locate, text):
        self.find_elements(types, locate).send_keys(text)
       # elements = self.find_elements(types, locate)
       # print(elements)
       # for element in elements:
       #     print(element)
       #     element.send_keys(text)

    # 清除值
    def clear_value(self, types, locate):
        self.find_elements(types, locate).clear()

    # 回车键
    def enter(self, types, locate):
        self.find_elements(types, locate).send_keys(Keys.ENTER)

    # 鼠标悬停
    def movetotargetelement(self, types, locate):
        ActionChains(self.driver).move_to_element(self.find_elements(types, locate)).perform()

    # 进入iframe
    def goto_iframe(self, types, locate):
        self.driver.switch_to.frame(self.find_elements(types, locate))

    # 返回iframe父窗口
    def out_frame_parent(self):
        self.driver.switch_to.parent_frame()

    # 返回iframe主窗口
    def out_frame(self):
        self.driver.switch_to.default_content()

    # 下拉框选择
    def choice_select_by_value(self, types, locate, value):
        # self.logger.info(f"选择下拉框: {types, locate}")
        Select(self.find_elements(types, locate)).select_by_index(value)

    # 关闭弹窗
    def alert_close(self):
        self.driver.switch_to.alert.accept()

    # 弹框警告-确认
    def alert_accept(self):
        # self.logger.info("弹框警告-确认")
        self.driver.switch_to.alert.accept()

    # 弹框警告-取消
    def alert_dismiss(self):
        # self.logger.info("弹框警告-取消")
        # self.driver.switch_to_alert().dismiss() 废弃的方式
        self.driver.switch_to.alert.dismiss()

    # 判断元素是否存在
    def is_element_exist(self, types, locate):
        # self.logger.info(f"判断元素是否存在: {types, locate}")
        flag = True
        try:
            self.find_elements(types, locate)
            return flag
        except:
            flag = False
            return flag

    # 获取当前url
    def web_url(self):
        """
        获取当前web_页面的URL
        :return:
        """
        url = self.driver.current_url
        self.logger.debug(f"获取当前url {url}")
        return url

    # 关闭浏览器驱动
    def quit(self):
        # self.logger.info("关闭浏览器驱动")
        self.driver.quit()

    # 获取页面元素
    def get_elements_from_yaml(self, yaml_file):
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
        return data.get('elements', [])

    # def get_by_type(self, types: str)
    #     """
    #     判断 APP or WEB   by类型
    #     :param types:   定位类型
    #     :return:
    #     """
    #     return self.web_by(types)

    def web_by(self, types: str):
        """
        获取定位类型
        :param types:  str  in(id,xpath,link_text/link,partial_link_text/partial,name,
        tag_name/tag,class_name/class,css_selector/css)
        :return:
        """
        if types == "id":
            return By.ID
        elif types == "xpath":
            return By.XPATH
        elif types == "link_text" or types == "link":
            return By.LINK_TEXT
        elif types == "partial_link_text" or types == "partial":
            return By.PARTIAL_LINK_TEXT
        elif types == "name":
            return By.NAME
        elif types == "tag_name" or types == "tag":
            return By.TAG_NAME
        elif types == "class_name" or types == "class":
            return By.CLASS_NAME
        elif types == "css" or types == "css_selector":
            return By.CSS_SELECTOR
        elif types == "function":
            return types
        else:
            raise Exception('定位类型错误！！！！')

    def web_execution(self, types, locate, text = None, notes =None, operate =None):

        types = self.web_by(types)

        if operate is None:
            self.logger.debug(notes)

        else:
            if operate == 'input':
                if operate is not None:
                    self.logger.debug(notes)
                    return self.send_key(types, locate, text)
                else:
                    self.logger.error('需传递text参数')

            elif operate == 'click':
                self.logger.debug(notes)
                return self.often_click(types, locate)

            elif operate == 'iframe':
                self.logger.debug(notes)
                return self.goto_iframe(types, locate)

            elif operate == 'frame_parent':
                self.logger.debug(notes)
                return self.out_frame_parent()

            elif operate == 'out_frame':
                self.logger.debug(notes)
                return self.out_frame()

            elif operate == 'select':
                self.logger.debug(notes)
                return self.choice_select_by_value(types, locate)

            elif operate == 'clear':
                self.logger.debug(notes)
                return self.clear_value(types, locate)

            elif operate == 'get_url':
                self.logger.debug(notes)
                return self.web_url()

    def web_exe(self, yaml_file, case_data, text=None):

        yaml = replace_py_yaml(yaml_file)

        locator_data = self.get_case(yaml, case_data)


        locator_step = locator_data.stepCount()

        for locator in range(locator_step):

            if locator_data.operate(locator) in ('input'):
                self.web_execution(types=locator_data.types(locator),
                                   locate=locator_data.locate(locator),
                                   operate=locator_data.operate(locator),
                                   text=text,
                                   notes=locator_data.info(locator)
                                   )

            else:
                self.web_execution(types=locator_data.types(locator),
                                   locate=locator_data.locate(locator),
                                   operate=locator_data.operate(locator),
                                   notes=locator_data.info(locator))

    def get_case(self, yaml_names=None, case_names=None):
        """
        获取用例数据   如果 case_names 以 test_ 开头直接找 caseYAML 目录下  如果不是 找 locaotrTAML
        :param yaml_names: ymal 路径
        :param case_names:  用例名称
        :return:
        """
        if yaml_names is not None:

            d = GetCaseYmal(yaml_name=yaml_names, case_name=case_names)
            return d
        else:
            raise Exception('yaml路径不能为空！')

