#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-


import allure
import pytest

from common.excle_export import excle_read
from pageobject.episodes_page import EpisodesPage

@allure.feature('剧集管理模块')
@pytest.mark.usefixtures('beginandend')
class Testeposodes:

    # 新增剧集
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集用例'))
    # def test_add_episodes(self, data, beginandend):
    #     for i in range(len(data)):
    #         if data[i] is None:
    #             data[i] = 'null'
    #     test_num, episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state, result = data
    #     self.driver, self.logger = beginandend
    #     ae = EpisodesPage(self.driver)
    #     ae.add_episodes(episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state)

    # # 新增分类
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集分类用例'))
    # def test_add_eposode_cate(self,data,beginandend):
    #     for i in range(len(data)):
    #         if data is None:
    #             data[i] = 'null'
    #     test_num, cate_name, parent_id, sort, status, result = data
    #     self.driver, self.logger = beginandend
    #     ac = EpisodesPage(self.driver)
    #     ac.add_cate(cate_name, parent_id, sort, status)
    # 新增剧集文件
    @allure.story('新增文件')
    @allure.title("测试标题")
    @allure.description('测试描述')
    @pytest.mark.usefixtures('beginandend')
    @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集文件用例'))
    def test_add_file(self, data, beginandend):
        for i in range(len(data)):
            if data[i] is None:
                data[i] = 'null'
        test_num, id, name, desc, sort, is_charge, price, vip_price, num, status, result = data
        self.driver, self.logger = beginandend
        af = EpisodesPage(self.driver, self.logger)
        af.add_file(id, name, desc, sort, is_charge, price, vip_price, num, status)
        # self.logger('新增文件用例'+test_num)




