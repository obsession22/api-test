#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-


import allure
import pytest

from common.excle_export import excle_read
from pageobject.login_page import Login


@allure.feature('剧集管理模块')
@pytest.mark.usefixtures('beginandend')
class Testedemo:
    @allure.story('新增文件')
    @allure.title("测试标题")
    @allure.description('测试描述')
    @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', 'demo'))
    def test_add_file(self,  beginandend):

        # for i in range(len(data)):
        #     if data[i] is None:
        #         data[i] = 'null'
        # case_num, title =data
        self.driver, self.logger = beginandend
        l = Login(self.driver, self.logger)
        l.login(self)