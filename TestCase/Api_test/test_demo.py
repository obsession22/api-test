"""
-*- coding: utf-8 -*-

@Author : fmz
@Time : 2023/9/7 14:14
@File : test_demo.py
"""
import allure
import pytest
import yaml
from common.excle_export import read_all_excel_data
from Api.base_api import BaseApi


# @pytest.mark.usefixtures('api_log')
# @allure.feature('后台模块api')
# class TestDemo:
#     @pytest.mark.parametrize('excel_data', read_all_excel_data('./data/api_test.xlsx'))
#     def test_api(self, excel_data, api_log):
#         api = BaseApi(api_log)
#         api.api()
