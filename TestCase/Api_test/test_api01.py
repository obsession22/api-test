# -*- coding: utf-8 -*-

import allure
import pytest
import yaml

from utils.get_yaml_data import YamlData
from Api.base_api import BaseApi
"""
@Author : fmz
@Time : 2024/2/27 15:13
@File : test_api01.py
"""
@pytest.mark.usefixtures('api_log')
@allure.feature('后台模块api')
class Testapi:


    @allure.story("用户登录api")
    @pytest.mark.parametrize('data', YamlData.get_data(r"C:\UIauto\WebUIAutoTest-master\data\locator_yml\test.yml"))
    def test_api(self, data, api_log):
        print(data)
        BaseApi.base_api(data, api_log)



