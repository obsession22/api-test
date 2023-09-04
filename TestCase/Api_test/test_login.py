# # -*- coding: utf-8 -*-
import json

import allure
import pytest
import yaml

from common.excle_export import excle_read
from Api.base_api import BaseApi


@allure.feature('登录模块api')
class Testapi:


    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', 'Sheet1'))
    def test_api(self, data):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        headers = json.loads(headers)
        request_data = json.loads(request_data)
        api = BaseApi()
        get_token = api.api(url=url, method=method, headers=headers, json=request_data).json()

        print(get_token)