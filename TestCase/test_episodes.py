#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-
import time
import traceback

import allure
import pytest

from common.excle_export import excle_read

from pageobject.episodes_page import EpisodesPage


# @pytest.mark.usefixtures('beginandend')
# @allure.feature('剧集管理模块')
# class Testeposodes1:
#
#     @pytest.mark.usefixtures('beginandend')
#     @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集用例'))
#     def test_add_eposode(self, data, beginandend):
#         for i in range(len(data)):
#             if data[i] is None:
#                 data[i] = 'null'
#         test_num, episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state, result = data
#         self.driver, self.logger = beginandend
#         ae = EpisodesPage(self.driver)
#         ae.add_episodes(episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state)
