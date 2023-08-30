# #!/usr/bin/env python
# # -*-coding:utf-8 -*-
# # -*- coding: utf-8 -*-
#
#
# import allure
# import pytest
#
# from common.excle_export import excle_read
# from pageobject.episodes_page import EpisodesPage
#
#
# @pytest.mark.usefixtures('beginandend')
# @allure.feature('剧集管理模块')
# class Testlogin:
#
#     @pytest.mark.usefixtures('beginandend')
#     @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增剧集文件用例'))
#     def test_add_file(self, data, beginandend):
#         for i in range(len(data)):
#             if data[i] is None:
#                 data[i] = 'null'
#         test_num, id, name, desc, sort, is_charge, price, vip_price, num, status, result = data
#         self.driver, self.logger = beginandend
#         af = EpisodesPage(self.driver)
#         af.add_file(id, name, desc, sort, is_charge, price, vip_price, num, status)
#         # self.logger('新增文件用例'+test_num)