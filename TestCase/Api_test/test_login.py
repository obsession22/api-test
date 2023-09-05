# # -*- coding: utf-8 -*-
import json

import allure
import pytest
import yaml

from common.excle_export import excle_read
from Api.base_api import BaseApi


@pytest.mark.usefixtures('api_log')
@allure.feature('后台模块api')
class Testapi:

    @allure.story("用户登录api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', 'Sheet1'))
    def test_api(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num, case_title=case_title, url=url, method=method, headers=headers, parameter_type=parameter_type, request_data=request_data).json()
        token = result["data"]["token"]
        code = result['code']

        assert code == 200, '状态码code不为200'
        if code == 200:
            # 读取yml
            with open("config.yaml", "r", encoding='utf-8') as yaml_file:
                config_data = yaml.safe_load(yaml_file)
            # 更新token的值
            config_data["API"]["token"] = token
            # 写入token
            with open("config.yaml", "w", encoding='utf-8')as yaml_file:
                yaml.dump(config_data, yaml_file, default_flow_style=False)

    @allure.story("获取用户权限api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', 'Sheet2'))
    def test_api1(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num, case_title=case_title, url=url, method=method, headers=headers, parameter_type=parameter_type, request_data=request_data)

    @allure.story("查询广告数据api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '广告数据用例'))
    def test_api2(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num, case_title=case_title, url=url, method=method, headers=headers, parameter_type=parameter_type, request_data=request_data).json()

    @allure.story("修改个人信息api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '修改个人信息'))
    def test_update_info(self, data, api_log):

        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num, case_title=case_title, url=url, method=method, headers=headers,
                         parameter_type=parameter_type, request_data=request_data).json()

    @allure.story("查询素材管理信息api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '查询素材管理信息'))
    def test_query_materials_manager(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data

        api = BaseApi(api_log)
        result = api.api(case_num=case_num,
                         case_title=case_title,
                         url=url, method=method,
                         headers=headers,
                         parameter_type=parameter_type,
                         request_data=request_data).json()

    @allure.story("查询授权账号信息api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '查询授权账号'))
    def test_query_account_authorization(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num,
                         case_title=case_title,
                         url=url, method=method,
                         headers=headers,
                         parameter_type=parameter_type,
                         request_data=request_data).json()

    @allure.story("查询计划数据api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '查询计划数据'))
    def test_query_plan(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num,
                         case_title=case_title,
                         url=url, method=method,
                         headers=headers,
                         parameter_type=parameter_type,
                         request_data=request_data).json()

    @allure.story("查询账号数据api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '查询账号数据'))
    def test_query_account(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data, assertion_condition, assertion_message = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num,
                         case_title=case_title,
                         url=url, method=method, assertion_message=assertion_message,
                         headers=headers, assertion_condition=assertion_condition,
                         parameter_type=parameter_type,
                         request_data=request_data).json()
        # print(assertion_condition)
        # assert eval(assertion_condition), assertion_message

    @allure.story("查询素材数据api")
    @pytest.mark.parametrize('data', excle_read('./data/api_test.xlsx', '查询素材数据'))
    def test_query_materials(self, data, api_log):
        case_num, case_title, headers, method, url, parameter_type, request_data = data
        api = BaseApi(api_log)
        result = api.api(case_num=case_num,
                 case_title=case_title,
                 url=url, method=method,
                 headers=headers,
                 parameter_type=parameter_type,
                 request_data=request_data).json()


