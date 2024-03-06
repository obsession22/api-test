# -*- coding: utf-8 -*-
"""
@Author : fmz
@Time : 2024/2/27 14:11
@File : get_yaml_data.py
"""
import yaml


class YamlData:
    def get_data(file_path):
        print(file_path)
        with open(file_path,encoding='UTF-8') as file:

            data = yaml.safe_load(file)
            return data
# if __name__ == '__main__':
#     data = YamlData.__init__(file_path=r"C:\UIauto\WebUIAutoTest-master\data\test_demo\test.yml")
#     print(data)
#     # data = YamlData.__init__(r"C:\UIauto\WebUIAutoTest-master\config.yaml")
#     # print(data)