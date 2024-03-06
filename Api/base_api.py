# -*- coding:utf-8 -*-

import allure
import requests

from utils.utils import Utils


class BaseApi:

    @staticmethod
    def send_request(method, url, headers=None, params=None, data=None, json=None, cookies=None):
        request_methods = {
            "GET": requests.get,
            "POST": requests.post,
        }
        request_func = request_methods[method]
        result = request_func(url, headers=headers, params=params, data=data, json=json, cookies=cookies)

        if method not in request_methods:
            raise ValueError("无效的请求方式: {}".format(method))

        return result

    # new
    @staticmethod
    def base_api(data, api_log):

        # 用例数据
        case_num = data['case_name']  # 用例编号
        case_title = data['case_title']  # 用例标题
        case_description = data['description']
        headers = data['headers']   # 请求头
        method = data['request_method']  # 请求方法
        url = data['url']  # 请求路径
        # 替换数据
        data_case = Utils.handle_request_data(data)
        request_data = data_case['request_data']  # 请求参数
        allure.dynamic.title(case_title)
        allure.dynamic.description(case_description)
        if "api_name" in data:
            allure.dynamic.story(data["api_name"])

        print(data_case)
        cookies = {}
        # cookies 设置
        if 'cookie' in data_case:
            cookies = Utils.cookie
        result = BaseApi.send_request(method=method, url=url, headers=headers, data=request_data, cookies=cookies)
        # 前置参数提取
        if 'extract' in data_case:
            Utils.extract(data_case['extract'], result)
        # 断言
        if 'validate' in data_case:
            validate_list = data_case['validate']
            Utils.validate(validate_list, result.json(), api_log)

        api_log.info("接口返回值： "+str(result.json()))
        return result.json()

