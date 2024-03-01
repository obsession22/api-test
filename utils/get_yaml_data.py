# -*- coding: utf-8 -*-
"""
@Author : fmz
@Time : 2024/2/27 14:11
@File : get_yaml_data.py
"""
import yaml


class YamlData:

    # def __init__(file_path):
    #     with open(file_path,encoding='UTF-8') as file:
    #         data = yaml.safe_load(file)
    #         return data

    def get_data(file_path):
        with open(file_path,encoding='UTF-8') as file:
            data = yaml.safe_load(file)
            return data
if __name__ == '__main__':
    data = YamlData.__init__(file_path=r"C:\UIauto\WebUIAutoTest-master\data\locator_yml\test.yml")
    print(data)
    # data = YamlData.__init__(r"C:\UIauto\WebUIAutoTest-master\config.yaml")
    # print(data)