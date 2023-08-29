#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-

import time


from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.config_util import get_yaml_config
from pageobject.table_commit import LoginPage

# 导航栏元素
# 剧集管理
episodes_mg_title_key = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[6]')
# 剧集
episodes_title_key = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[6]/dl/dd[2]/a')

# 页面元素
episodes_iframe = (By.XPATH, '//*[@id="353"]')
episodes_add_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')

# 新增页面
episodes_iframe2 = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
episodes_add_name = (By.XPATH, '//*[@id="name"]')
cover_button = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div[2]/div[2]')
tips_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[12]/div/div/xm-select')
tips = (By.XPATH, '/html/body/form/div[1]/div/div/div[12]/div/div/xm-select/div[3]/div/div/div[2]/div/div')
desc_key = (By.XPATH, '//*[@id="desc"]')
sort_key = (By.XPATH, '//*[@id="sort"]')
cate_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[5]/div/div')
cate_next_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[5]/div/div/xm-select/div[3]/div/div/div[2]/div/div')
price_key =(By.XPATH, '//*[@id="price"]')
vip_price_key =(By.XPATH, '//*[@id="vip_price"]')
number_key = (By.XPATH, '//*[@id="total_num"]')
wx_drama_id_key = (By.XPATH, '//*[@id="wx_drama_id"]')
hide_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[10]/div/div/em')
state_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[11]/div/div/em')
submit_key = (By.XPATH, '/html/body/form/div[2]/div/button[1]')

# 封面iframe
cover_iframe = (By.CSS_SELECTOR, '#layui-layer-iframe2')
id_key = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[1]/div')
ok_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[2]')

# 分类页面元素
cate_iframe = (By.XPATH, '//*[@id="264"]')
cate_add_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')
name_cate = (By.XPATH, '//*[@id="cate_name"]')
id_parent = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div/xm-select')
parent_id_value = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div/xm-select/div[3]/div/div[1]/input')
parent_id_select_1 = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div/xm-select/div[3]/div/div[2]/div[1]/div')
cate_sort = (By.XPATH, '//*[@id="sort"]')
cate_status =(By.XPATH, '/html/body/form/div[1]/div/div/div[4]/div/div/em')
add_submit = (By.XPATH, '/html/body/form/div[2]/div/button[1]')

# 新增文件
file_title = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[6]/dl/dd[3]/a')
file_iframe = (By.XPATH, '//*[@id="364"]')
file_add_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')
episodes_id = (By.XPATH, '/html/body/form/div[1]/div/div/div[1]/div/div/xm-select')
episodes_id_1 = (By.XPATH, '/html/body/form/div[1]/div/div/div[1]/div/div/xm-select/div[3]/div/div/div[2]/div[1]/div')
episodes_id_query = (By.XPATH, '/html/body/form/div[1]/div/div/div[1]/div/div/xm-select/div[3]/div/div/div[1]/input')

# file_add_iframe = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
episodes_name = (By.XPATH, '//*[@id="name"]')
episodes_desc = (By.XPATH, '//*[@id="desc"]')
episodes_sort = (By.XPATH, '//*[@id="sort"]')
charge = (By.XPATH, '/html/body/form/div[1]/div/div/div[6]/div/div/em')
episodes_price = (By.XPATH, '//*[@id="price"]')
episodes_vip_price = (By.XPATH, '//*[@id="vip_price"]')
episodes_num = (By.XPATH, '//*[@id="num"]')
episodes_status = (By.XPATH, '/html/body/form/div[1]/div/div/div[11]/div/div/em')


# 剧集页面
class EpisodesPage(BasePage):

    # 新增剧集
    def add_episodes(self, episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state):
        LoginPage.login(self)
        self.click(episodes_mg_title_key)
        time.sleep(1)
        self.click(episodes_title_key)
        self.goto_frame(episodes_iframe)
        self.click(episodes_add_button)
        time.sleep(1)
        # 切换到下一级iframe
        self.goto_frame(episodes_iframe2)
        if episodes_name != 'null':
            self.send_keys(episodes_add_name, episodes_name)
        self.click(cover_button)
        print(cover_iframe)
        self.goto_frame(cover_iframe)
        self.click(id_key)
        self.click(ok_button)
        # 返回上一级
        self.out_frame_parent()
        if desc != 'null':
            self.clear(desc_key)
            self.send_keys(desc_key, desc)
        if sort != 'null':
            self.clear(sort_key)
            self.send_keys(sort_key, sort)
        # if cate_id != 'null':
        #     self.send_keys()
        self.click(cate_key)
        self.click(cate_next_key)
        if price != 'null':
            self.clear(price_key)
            self.send_keys(price_key, price)
        if vip_price != 'null':
            self.clear(vip_price_key)
            self.send_keys(vip_price_key, vip_price)
        if number != 'null':
            self.clear(number_key)
            self.send_keys(number_key, number)
        if wx_drama_id != 'null':
            self.clear(wx_drama_id_key)
            self.send_keys(wx_drama_id_key, wx_drama_id)
        if hide == 1:
            self.click(hide_key)
        if state == 1:
            self.click(state_key)
        self.click(tips_key)
        self.click(tips)
        self.click(submit_key)

    # 新增分类
    def add_cate(self, cate_name, parent_id, sort, status):
        LoginPage.login(self)
        self.click(episodes_mg_title_key)
        time.sleep(1)
        self.goto_frame(cate_iframe)
        self.click(cate_add_button)
        self.goto_frame(episodes_iframe2)
        self.send_keys(name_cate, cate_name)

        if parent_id != 'null':
            if parent_id == 1:
                self.click(id_parent)
                self.send_keys(parent_id_value, '剧情')
                self.click(parent_id_select_1)

        if sort != 'null':
            self.clear(cate_sort)
            self.send_keys(cate_sort, sort)
        time.sleep(1)
        if status == 1:
            self.click(cate_status)
        self.click(add_submit)

        # 新增剧集文件
    def add_file(self, episode_id, name, desc, sort, is_charge, price, vip_price, num, status):

        LoginPage.login(self)
        self.click(episodes_mg_title_key)
        time.sleep(1)
        self.click(file_title)
        self.goto_frame(file_iframe)
        self.click(file_add_button)

        self.goto_frame(episodes_iframe2)
        if episode_id != 'null':
            self.click(episodes_id)
            self.send_keys(episodes_id_query,episode_id)
            self.click(episodes_id_1)
        else:
            self.click(episodes_id)
            self.click(episodes_id_1)
        if name != 'null':
            self.send_keys(episodes_name, name)
        if desc != 'null':
            self.send_keys(episodes_desc, desc)
        if sort != 'null':
            self.clear(episodes_sort)
            self.send_keys(episodes_sort, sort)
        time.sleep(1)
        if is_charge == 1:
            self.click(charge)
        if price != 'null':
            self.clear(episodes_price)
            self.send_keys(episodes_price, price)
        if vip_price != 'null':
            self.clear(episodes_vip_price)
            self.send_keys(episodes_vip_price, vip_price)
        if num != 'null':
            self.clear(episodes_num)
            self.send_keys(episodes_num, num)
        if status == 1:
            self.click(episodes_status)
        time.sleep(3)







