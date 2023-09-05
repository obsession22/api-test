# -*- coding:utf-8 -*-

import requests
import json as json_util
from config.config_util import get_yaml_config


class BaseApi:
    def __init__(self, logger):
        self.logger = logger

    def base_get(self, url, headers=None, params=None):
        result = requests.get(url, headers=headers, params=params)
        # 日志输出返回值
        if result is not None:
            self.logger.info(result.json())
            return result
        else:
            self.logger.error("请求失败，没接收到返回值，请检查用例格式是否填写正确")

    def base_post(self, url, headers=None, data=None, json=None, assertion=None):
        result = requests.post(url, json=json, data=data, headers=headers)
        # 执行断言

        # 日志输出返回值
        if result is not None:
            self.logger.info(result.json())
            return result
        else:
            self.logger.error("请求失败，没接收到返回值，请检查用例格式是否填写正确")

    def api(self, case_num, case_title, method, url,  parameter_type, assertion_message=None, assertion_condition=None, headers=None, request_data=None):

        self.logger.info('用例编号：'+case_num)
        self.logger.info('用例标题：'+case_title)

        # 在请求头中设置token
        token = get_yaml_config('API', 'token')
        headers = json_util.loads(headers)
        headers['Authorization'] = f'Bearer {token}'

        # 拼接请求地址 环境地址 + 请求路径
        environment = get_yaml_config('environment', 'test_url')
        url = environment + url

        # 转换类型
        if request_data is not None:
            request_data = json_util.loads(request_data)

        json = None
        params = None
        data = None

        # 判断传参类型
        if parameter_type == 'json':
            json = request_data
        elif parameter_type == 'params':
            params = request_data
        elif parameter_type == 'data':
            data = request_data
        if method == 'GET':
            result = self.base_get(url, headers=headers, params=params)
            if assertion_condition is not None:
                assert eval(assertion_condition), assertion_message
            return result
        elif method == 'POST':
            result = self.base_post(url, headers=headers, data=data, json=json)
            if assertion_condition is not None:
                assert eval(assertion_condition), assertion_message
            return result
        else:
            self.logger.error('用例编号：'+case_num+'标题：'+case_title+'执行出错，检查用例的请求类型是否为GET或POST')
