import json

import re
from hamcrest import *


class Utils:

    extracted_variables = {}  # 存储提取的变量

    cookie = {}  # cookie

    @staticmethod
    def handle_request_data(request_data: dict):
        """
        接口依赖数据填充   先用正则提取需要替换的数据，在根据每个替换的key提取出value
        :param request_data: 请求的数据
        :return: 返回替换后的request_data
        """
        request_data = json.dumps(request_data)
        regex = r"\$\{(.+?)\}"
        regex_obj = re.compile(regex)
        replace_values = regex_obj.findall(request_data)
        for val in replace_values:
            key = val  # 变量名就是占位符中的内容
            value = Utils.extracted_variables.get(key)
            if value is not None:
                request_data = request_data.replace(f"${{{key}}}", value)
        return json.loads(request_data)

    @staticmethod
    def extract(extract_rules: dict, response: dict):
        """
        提取接口返回值的变量并存储
        :param extract_rules: 提取的目标
        :param response:  接口返回值
        :return:
        """

        for key, value_path in extract_rules.items():
            # 判断提取的值是否有cookie
            if key == 'cookie':
                Utils.cookie = response.cookies.get_dict()
                continue
            extracted_value = Utils.get_value_from_response(value_path, response.json())
            Utils.extracted_variables[key] = extracted_value

    @staticmethod
    def get_value_from_response(value_path: str, response: dict):
        # 从响应结果中根据值路径提取对应的值
        # 这里的示例代码仅支持简单的值路径，如 "data.token"
        """
        根据响应值路径提取对应的值
        :param value_path:提取值的路径
        :param response:响应结果
        :return:响应结果中提取的值
        """

        # $.data.level
        separators = ['$', '.', ' ']
        for separator in separators:
            value_path = value_path.replace(separator, ' ')
        keys = value_path.split()
        extracted_value = response
        for key in keys:

            extracted_value = extracted_value.get(key)

            if extracted_value is None:
                break
        return extracted_value

    @staticmethod
    def validate(validate_list: list, response, log):
        assertions = {
            "equal_to": equal_to,
            "less_than": less_than,
            "greater_than": greater_than,
            "has_length": has_length,
            "has_string": has_string,
            "greater_than_or_equal_to": greater_than_or_equal_to,
            "less_than_or_equal_to": less_than_or_equal_to,
        }

        #[{'equal_to': {'.data.id': 159395, '.data.admin': False, '.data.nickname': 'sanhai'}}, {'equal_to': {'.errorCode': 0}}]
        for validate in validate_list:
            #'equal_to' {'.data.id': 159395, '.data.admin': False, '.data.nickname': 'sanhai'}
            for key, item in validate.items():
                for key_json_path, item_expect in item.items():
                    # key_json_path 是断言的目标 如（$.data.id）等等
                    # 通过测试用例中的断言参数，从response中提取对应的值
                    # actual_val 从实际接口返回断言参数的值
                    # item_expect 断言目标值
                    actual_val = Utils.get_value_from_response(key_json_path, response)

                    if key in assertions:
                        # 执行断言 key_json_path + item_expect + key_json_path + key +actual_val
                        log.info("执行断言"+key_json_path+"="+str(item_expect)+" "+key+" "+key_json_path+"="+str(actual_val))
                        assert_func = assertions[key]
                        assert_that(actual_val, assert_func(item_expect))
                    else:
                        log.error("不存在该断言，请检查用例")
