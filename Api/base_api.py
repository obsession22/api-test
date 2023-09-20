# -*- coding:utf-8 -*-
import allure
import pytest
import requests
import json as json_util
from config.config_util import get_yaml_config
from common.excle_export import write_case_result


class BaseApi:
    def __init__(self, logger):
        self.logger = logger

    def send_request(self, method, url, headers=None, params=None, data=None, json=None):
        request_methods = {
            "GET": requests.get,
            "POST": requests.post,
        }
        request_func = request_methods[method]
        result = request_func(url, headers=headers, params=params, data=data, json=json)

        if method not in request_methods:
            raise ValueError("无效的请求方式: {}".format(method))

        if result is not None:
            self.logger.info("接口返回值：" + str(result.json()))
            return result
        else:
            self.logger.error("请求失败，没接收到返回值，请检查用例格式是否填写正确")

    def api(self, data, sheet_name):
        # def api(self, case_num, case_title, method, url, parameter_type,
        #         assertion_condition=None, headers=None, request_data=None, sheet_name=None):
        # 用例数据
        case_num = data[0]  # 用例编号
        case_title = data[1]  # 用例标题
        headers = data[2]   # 请求头
        method = data[3]  # 请求方法
        url = data[4]  # 请求路径
        parameter_type = data[5]  # 参数类型
        request_data = data[6]  # 请求参数
        assertion_condition = data[7]  # 断言
        case_status = data[8]   # 状态
        """
        get、post通用api
        :param case_num: 测试用例编号
        :param case_title: 测试用例标题
        :param method: 请求方法
        :param url: 请求路径
        :param parameter_type: 参数类型
        :param assertion_condition: 断言
        :param headers: 请求头
        :param request_data: 请求参数
        :param sheet_name: 工作表名
        :param data: data
        :return:
        """
        # 测试数据excel所在路径
        path = get_yaml_config('test_excel_data', 'path')
        # 在请求头中设置token
        token = get_yaml_config('API', 'token')
        try:
            headers = json_util.loads(headers)
        except:
            write_case_result(path, sheet_name, case_num, case_status='failed')
        headers['Authorization'] = f'Bearer {token}'

        # 拼接请求地址 环境地址 + 请求路径
        environment = get_yaml_config('environment', 'test_url')
        url = environment + url

        # 用例标题
        allure.dynamic.title(case_title)

        self.logger.info('用例编号：'+case_num)
        self.logger.info('用例标题：'+case_title)
        if assertion_condition is not None:
            self.logger.info('断言表达式：' + assertion_condition)
        if parameter_type is not None:
            self.logger.info("参数类型："+parameter_type)
        else:
            self.logger.info("参数类型为None")
        self.logger.info("请求参数："+str(request_data))
        self.logger.info("请求类型：" + method)
        self.logger.info("请求地址："+url)
        # 转换类型
        if request_data is not None:
            request_data = json_util.loads(request_data)
        json_data = None
        params = None
        data = None

        # 判断传参类型
        if parameter_type == 'json':
            json_data = request_data
        elif parameter_type == 'params':
            params = request_data
        elif parameter_type == 'data':
            data = request_data

        result = self.send_request(method, url, headers=headers, params=params, data=data, json=json_data)

        # if assertion_condition is not None:
        #     assert eval(assertion_condition), assertion_message

        if assertion_condition is not None:
            assertions = json_util.loads(assertion_condition)
            # 迭代执行断言条件
            for assertion in assertions:
                condition = assertion.get('condition')
                message = assertion.get('message')
                if condition is not None:
                    try:
                        assert eval(condition), message
                        write_case_result(path, sheet_name, case_num, case_status='pass')
                    except AssertionError as e:
                        write_case_result(path, sheet_name, case_num, case_status='failed')
                        raise e
        return result

