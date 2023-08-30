"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : conftest.py
@Author : putongrenji
@Time : 2022/5/4 11:17
@Motto:Don't ever let somebody tell you you can't do something
"""
import coloredlogs
import pytest
from selenium import webdriver
from utils.logger_util import LoggerUtil
from utils.config_util import get_config_browser

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
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    yield (driver,logger)
    print()
    logger.info("----------测试用例执行结束----------\n")
    driver.quit()
    lu.remove_handler()