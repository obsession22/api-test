# -*- coding: utf-8 -*-
import os
import pickle
from typing import List, Tuple
from config import CASEYMAL_DIR, LOCATORYMAL_DIR
import yaml

class GetCaseYmal:
    def __init__(self, yaml_name: str, case_name: str = None) -> None:
        """
        :param yaml_name:  yaml 文件名称
        :param case_name:  用列名称 对应 yaml 用列
        """
        # 读取配置参数

        self.yaml_name = yaml_name  # yaml 文件名称 拼接后的路径

        if case_name is not None:  # 如果用例名称不为空 可自动识别读取定位数据还是测试数据
            self.modelname = yaml_name  # 模块名称 对应yaml 文件名
            self.case_name = case_name  # 用列名称 对应 yaml 用列

            if case_name.startswith('test'):
                self.FLIE_PATH = os.path.join(CASEYMAL_DIR, f"{self.yaml_name}")
            else:
                self.FLIE_PATH = os.path.join(LOCATORYMAL_DIR, f"{self.yaml_name}")
        else:  # 没有用例名称 直接返回定位用例yaml路径
            self.FLIE_PATH = os.path.join(LOCATORYMAL_DIR, f"{self.yaml_name}")

    def open_yaml(self):
        """
        读取yaml文件
        :return: dict
        """
        try:
            with open(self.FLIE_PATH, encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                f.close()
                return data
        except UnicodeDecodeError:
            with open(self.FLIE_PATH, encoding='GBK') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                f.close()
                return data

    def get_yaml(self):
        """
        返回yaml文件数据
        :return: dict
        """
        yaml_data = self.open_yaml()
        if yaml_data is not None:
            return yaml_data[1:]  # 返回用列数据不包含 - model : login 部分 从列表1位置索引
        else:
            raise ('The ymal file is empty')

    def get_current_data(self):
        """
        返回 yaml 当前用列的所有数据
        :return: dict
        """
        yamlList = self.get_yaml()
        for yaml in yamlList:
            # 如果用列等于当前 用列就返回
            if yaml.get('casename') == self.case_name:
                return yaml
        return "casename 不存在！"

    def count_test_data(self):
        """
        统计 yaml  data 测试数据的条数
        :return:
        """
        yaml_list = self.get_yaml()
        for yaml in yaml_list:
            # 如果用列等于当前 用列就返回
            if yaml.get('casename') == self.case_name:
                try:
                    testdata_len = len(yaml.get('testdata'))
                    return testdata_len
                except Exception as e:
                    pass

    def dataCount(self):
        """
        统计 data  数据条数
        :return:
        """
        return self.count_test_data()
    def stepCount(self):
        """
        统计 yaml 测试步骤条数
        :return:
        """
        dataList = self.get_yaml()

        if dataList:
            for data in dataList:
                # 如果用列等于当前 用列就返回
                if data.get('casename') == self.case_name:
                    return len(data.get('element'))
        else:
            raise Exception('用例不存在！请检查文件')

    def get_param(self, value: str) -> str:
        """
        获取 yaml用列参数
        :param value:  传递参数值
        :return:
        """

        yamlList = self.get_yaml()
        for yaml in yamlList:
            # 如果用列等于当前 用列就返回
            if yaml.get('casename') == self.case_name:
                return yaml.get(value)
        return "casename 不存在！"

    def get_set(self, index: int, vaule: str):
        """
        获取 set 用列步骤数据

        :param index: 列表索引位置
        :param vaule:  参数值
        :return:
        """
        # 如果读取redis 就从redis获取数据 否则从yaml获取

        dataList = self.get_yaml()
        if index < self.stepCount():
            for data in dataList:
                # 如果用列等于当前 用列就返回
                if data.get('casename') == self.case_name:
                    return data.get('element')[index].get(vaule)
        # logger.error(f'{self.case_name}用列只有{self.stepCount()}个步骤，你确输入了{index} 步！')
        return None

    def operate(self, index: int) -> str:
        """
        返回 用列步骤 operate 参数
        """
        return self.get_set(index, 'operate')

    def locate(self, index: int) -> str:
        """
        返回 用列步骤 locate 参数
        """
        return self.get_set(index, 'locate')

    def types(self, index: int) -> str:
        """
        返回 用列步骤 types 参数
        """
        return self.get_set(index, 'types')

    def info(self, index: int) -> str:
        """
        返回 用列步骤 info 参数
        """
        return self.get_set(index, 'info')



def replace_py_yaml(file):
    """
    当前py文件转为 yaml后缀
    :param file:
    :return:
    """
    return os.path.basename(file).replace('py', 'yaml')
