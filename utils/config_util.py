"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : config_util.py
@Author : putongrenji
@Time : 2022/4/30 14:27
@Motto:Don't ever let somebody tell you you can't do something
"""
import os
import yaml
from selenium import webdriver


# 全局
def get_project_path():
    '''全局：获得项目路径'''
    realpath = os.path.dirname(os.path.dirname(__file__))
    return realpath

# 读取全部的yml数据
def read_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            yaml_data = yaml.safe_load(file)
            return yaml_data
        except yaml.YAMLError as e:
            print(f"Error while parsing YAML file: {e}")


# 读取yaml配置文件
def get_yaml_config(one_name,two_name):
    '''全局：读取全局配置yaml文件'''
    with open(str(get_project_path())+'\\' + 'config.yaml', 'r',encoding='utf-8') as f:
        # cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
        cfg = yaml.safe_load(f.read())
        return cfg[one_name][two_name]


# 获得配置文件config.yaml中的浏览器信息，返回driver对象。
def get_config_browser():
    browser_name = get_yaml_config('browser','browser_name')
    global driver
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()
    return driver


if __name__ == '__main__':
    # print(get_project_path())
    # print(get_yaml_config("browser","browser_name"))
    data1 = read_yaml_file(r"C:\UIauto\WebUIAutoTest-master\data\locator_yml\test.yml")
    print(data1[1]["name"])