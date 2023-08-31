#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-


import allure
import pytest

from common.excle_export import excle_read
from pageobject.episodes_page import EpisodesPage
from base.base_page import BasePage

# @allure.feature('剧集管理模块')
# @pytest.mark.usefixtures('beginandend')
# class Testedemo:
#     @allure.story('新增文件')
#     @allure.title("测试标题")
#     @allure.description('测试描述')
#     @pytest.mark.usefixtures('beginandend')
#     # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集文件用例'))
#     def test_add_file(self, beginandend):
#         # for i in range(len(data)):
#         #     if data[i] is None:
#         #         data[i] = 'null'
#
#         self.driver, self.logger = beginandend
#         p = BasePage(self.driver,self.logger)
#         p.webexe('./data/locator_yml/test.yml')
