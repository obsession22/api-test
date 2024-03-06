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
@allure.feature('业务模块：登录查询流程')
class Testapi:
    @pytest.mark.parametrize('data', YamlData.get_data("./data/test_demo/test.yml"))
    def test_api(self, data, api_log):
        print(data)
        BaseApi.base_api(data, api_log)



