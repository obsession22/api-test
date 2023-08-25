"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Author : putongrenji
@Time : 2022/4/25 15:41
"""
import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.config_util import get_yaml_config

# 账号密码
username = get_yaml_config('default_login', 'username')
password = get_yaml_config('default_login', 'password')

# 登录地址
login_url = get_yaml_config('url', 'login_url')
username_key = (By.XPATH, '/html/body/form/div[2]/input')
password_key = (By.XPATH, '/html/body/form/div[3]/input')
login_button = (By.XPATH, '/html/body/form/div[5]/button')

class LoginPage(BasePage):
    # 页面元素
    # username_key = (By.XPATH, '/html/body/form/div[2]/input')
    # password_key = (By.XPATH, '/html/body/form/div[3]/input')
    # login_button = (By.XPATH, '/html/body/form/div[5]/button')

    def login(self):
        self.get(login_url)
        time.sleep(2)
        self.send_keys(username_key, username)
        self.send_keys(password_key, password)
        self.click(login_button)
        time.sleep(1)

    # # 登录成功断言
    # def get_except_result_access(self):
    #     self.element_Wait(LoginPage.comm_access)
    #     return self.get_value(LoginPage.comm_access)
    #
    # # 登录失败断言
    # def get_except_result_fail(self):
    #     self.element_Wait(LoginPage.login_fail)
    #     return self.get_value(LoginPage.login_fail)


# 套餐页面
class packagePage(BasePage):
    # 账号密码
    # username = get_yaml_config('default_login', 'username')
    # password = get_yaml_config('default_login', 'password')
    #
    # username_key = (By.XPATH, '/html/body/form/div[2]/input')
    # password_key = (By.XPATH, '/html/body/form/div[3]/input')
    # login_button = (By.XPATH, '/html/body/form/div[5]/button')

    #导航栏元素
    package = (By.XPATH,'/html/body/div[1]/div[2]/div[3]/div/div/ul/li[4]/a')
    iframe = (By.XPATH, '//*[@id="378"]')
    #套餐新增页面元素
    add = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')
    duoxuan_01 = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div')
    update = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td/div/button[1]')
    query_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[2]')
    #页面输入框、按钮
    from_iframe = (By.XPATH,'//*[@id="layui-layer-iframe2"]')
    price_key = (By.XPATH, '//*[@id="price"]')
    gives_key = (By.XPATH, '//*[@id="give"]')
    description_key = (By.XPATH, '//*[@id="describe"]')
    text_key = (By.XPATH, '//*[@id="right_top"]')
    give_num_key = (By.XPATH, '//*[@id="give_num"]')
    submit_key = (By.XPATH, '/html/body/form/div[2]/div/button[1]')

    #删除套餐
    del_button = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[4]/div[2]/table/tbody/tr[1]/td/div/button[2]')
    button = (By.CSS_SELECTOR, '.layui-layer-btn0')
    del_iframe = (By.XPATH, '//*[@id="378"]')

    # 套餐搜索输入框
    id_key = (By.XPATH, '//*[@id="id"]')
    price_key = (By.XPATH, '//*[@id="price"]')
    give_key = (By.XPATH, '//*[@id="give"]')
    describe_key = (By.XPATH, '//*[@id="describe"]')
    top_key = (By.XPATH, '//*[@id="right_top"]')
    package_type = (By.XPATH, '//*[@id="type"]')
    num_key = (By.XPATH, '//*[@id="num"]')
    give_nums_key = (By.XPATH, '//*[@id="give_num"]')
    type_1 = (By.XPATH, '//*[@id="search-form"]/div/form/div/div[7]/div/div/div/input')
    query_key = (By.XPATH, '//*[@id="search-form"]/div/form/div/div[11]/button[1]')

    # 分组页面
    grp_if = (By.XPATH, '//*[@id="831198658211876929"]')
    grp_add = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')
    grp_ip = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[4]/dl/dd[2]/a')
    grp_title = (By.XPATH, '//*[@id="title"]')
    grp_from_if = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
    grp_drop_down = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div/xm-select')
    grp_drop_down_1 =(By.XPATH,'/html/body/form/div[1]/div/div/div[2]/div/div/xm-select/div[3]/div/div/div[2]/div[1]/div')
    grp_btn = (By.XPATH, '/html/body/form/div[1]/div/div/div[3]/div/div[2]/i')
    query_grp_key = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[2]')
    grp_Id_key = (By.XPATH, '//*[@id="id"]')
    grp_title_key = (By.XPATH, '//*[@id="title"]')
    grp_button = (By.XPATH, '//*[@id="search-form"]/div/form/div/div[4]/button[1]')
    del_grp = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/button[3]')
    del_grp_button =(By.CSS_SELECTOR, '#layui-layer7 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0')

    # 新增套餐
    def addPackage(self, price, gives, description, text, give_num,):

        LoginPage.login(self)
        self.click(self.package)
        # 切换iframe页面
        self.goto_frame(self.iframe)
        self.click(self.add)
        # time.sleep(1)
        # 切换到下一层iframe
        self.goto_frame(self.from_iframe)
        self.send_keys(self.price_key, price)
        self.send_keys(self.gives_key, gives)
        self.send_keys(self.description_key, description)
        self.send_keys(self.text_key, text)
        self.send_keys(self.give_num_key, give_num)
        self.click(self.submit_key)
        time.sleep(1)

    # 修改页面
    def update_package(self, price, gives, description, text, give_num):

        LoginPage.login(self)
        time.sleep(2)
        self.click(self.package)
        # 切换iframe页面
        self.goto_frame(self.iframe)
        self.click(self.duoxuan_01)
        print(self.update)
        self.click(self.update)
        time.sleep(1)
        # 切换到下一层iframe
        self.goto_frame(self.from_iframe)
        self.clear(self.price_key)
        self.send_keys(self.price_key, price)
        self.clear(self.gives_key)
        self.send_keys(self.gives_key, gives)
        self.clear(self.description_key)
        self.send_keys(self.description_key, description)
        self.clear(self.text_key)
        self.send_keys(self.text_key, text)
        self.clear(self.give_num_key)
        self.send_keys(self.give_num_key, give_num)
        self.click(self.submit_key)

    # 删除套餐
    def delete_package(self):

        LoginPage.login(self)
        time.sleep(5)
        self.click(self.package)
        # 切换iframe页面
        self.goto_frame(self.iframe)
        # print(11)
        # time.sleep(2)
        self.click(self.del_button)
        # time.sleep(2)
        self.click(self.button)
        # time.sleep(2)

    # 查询套餐
    def query_package(self,Id, price, give_text, description, corner, num, give_num):

        LoginPage.login(self)
        time.sleep(2)
        self.click(self.package)
        # 切换iframe页面
        self.goto_frame(self.iframe)
        self.click(self.query_button)
        if Id != 'null':
            self.send_keys(self.id_key, Id)
        if price != 'null':
            self.send_keys(self.price_key, price)
        if give_text != 'null':
            self.send_keys(self.give_key, give_text)
        if description != 'null':
            self.send_keys(self.describe_key, description)
        if corner != 'null':
            self.send_keys(self.top_key, corner)
        if num != 'null':
            self.send_keys(self.num_key, num)
        if give_num != 'null':
            self.send_keys(self.give_nums_key, give_num)
        # self.click(self.type_1)
        # self.maxWindows()
        # self.choice_select_by_value(self.package_type, 1)
        time.sleep(2)
        self.click(self.query_key)
        time.sleep(2)

    # 套餐分组
    # 新增分组
    def add_group(self, title_name):
        LoginPage.login(self)
        time.sleep(2)
        self.click(self.package)
        time.sleep(2)
        self.click(self.grp_ip)
        time.sleep(2)
        self.goto_frame(self.grp_if)
        self.click(self.grp_add)
        # 进入下一级iframe
        self.goto_frame(self.grp_from_if)
        self.send_keys(self.grp_title, title_name)
        time.sleep(2)
        self.click(self.grp_btn)
        time.sleep(2)
    # 分组查询
    def query_group(self, Id, title, type):
        LoginPage.login(self)
        time.sleep(2)
        self.click(self.package)
        time.sleep(2)
        self.click(self.grp_ip)
        time.sleep(2)
        self.goto_frame(self.grp_if)
        self.click(self.query_grp_key)
        if Id != 'null':
            self.send_keys(self.grp_Id_key, Id)
        if title != 'null':
            self.send_keys(self.grp_title_key,title)
        self.click(self.grp_button)
        # time.sleep(2)

    # 删除分组
    def del_group(self):
        LoginPage.login(self)
        time.sleep(2)
        self.click(self.package)
        time.sleep(2)
        self.click(self.grp_ip)
        self.goto_frame(self.grp_if)
        self.click(self.del_grp)
        self.click(self.button)


















