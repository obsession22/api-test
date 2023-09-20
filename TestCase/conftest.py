"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : conftest.py
@Author : putongrenji
@Time : 2022/5/4 11:17
@Motto:Don't ever let somebody tell you you can't do something
"""

import coloredlogs
import openpyxl
import pytest
from selenium import webdriver
from utils.logger_util import LoggerUtil
from utils.config_util import get_config_browser
from common.excle_export import excle_read


@pytest.fixture(name='beginandend')
def beginToend():
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.handlers.clear()
    # coloredlogs.install(level='DEBUG', logger=logger)
    coloredlogs.install(level='DEBUG', logger=logger,
                        level_styles={'info': {'color': 'green'},
                                      'warning': {'color': 'yellow'},
                                      'error': {'color': 'red'},
                                      'critical': {'color': 'red', 'bold': True}})
    logger.info("----------测试用例执行开始----------")
    global driver
    driver = get_config_browser()
    yield (driver,logger)
    print()
    logger.info("----------测试用例执行结束----------\n")
    driver.quit()
    lu.remove_handler()


@pytest.fixture(name='api_log')
def api_log():
    # print(request.param)
    lu = LoggerUtil()
    logger = lu.get_logger()
    logger.handlers.clear()
    coloredlogs.install(level='DEBUG', logger=logger,
                        level_styles={'info': {'color': 'green'},
                                      'warning': {'color': 'yellow'},
                                      'error': {'color': 'red'},
                                      'critical': {'color': 'red', 'bold': True}})
    logger.info("----------测试用例执行开始----------")
    yield logger
    # out = yield logger
    # report = out.get_result()
    # print(('运行结果: %s' % report.outcome))
    logger.info("----------测试用例执行结束----------\n")
    lu.remove_handler()


@pytest.fixture(name='test_data')
def test_data():
    excle_read()


#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     # 2. 获取钩子方法的调用结果
#     result = yield
#     print('钩子方法的执行结果', result)
#     print('item',item.name)
#     print('result',result.get_result)
    # print(request)
    # 3. 从钩子方法的调用结果中获取测试报告
    # report = result.get_result()
    # print(report)

    # sheet_mark = item.get_closest_marker('sheet')
    # sheet_name = sheet_mark.args[0]
    # print(item.name)
    # print(excle_read('./data/api_test.xlsx', 'Sheet1'))
    # write_case_result('./data/api_test.xlsx', sheet_name, report)
#     # print(sheet_name)
#     # print('------------------------------------')
#     # print('从结果中获取测试报告：', report)
#     # print('从报告中获取 nodeid：', report.nodeid)
#     # print('从报告中获取调用步骤：', report.when)
#     # print('从报告中获取执行结果：', report.outcome)


def write_case_result(excel_path, sheet_name, report):
    # 打开工作簿
    wb = openpyxl.load_workbook(excel_path)
    # 获取sheet对象
    sheet = wb[sheet_name]

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row):
        # 使用索引来访问行的数据
        if row[0].value == report.nodeid:
            row[8].value = report.outcome

    # 保存工作簿
    wb.save(excel_path)
    wb.close()


if __name__ == '__main__':
    print(excle_read('../data/api_test.xlsx', 'Sheet1'))
    # write_case_result('../data/api_test.xlsx','Sheet1')