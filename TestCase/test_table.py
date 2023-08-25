#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-

import time
import traceback

import allure
import pytest
from common.excle_export import excle_read
from pageobject.table_commit import LoginPage
from pageobject.table_commit import packagePage


@pytest.mark.usefixtures('beginandend')
@allure.feature('测试后台')
class Testtable1:

    #@pytest.mark.skip('测试阶段')
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', 'Sheet1'))
    # def test_table_01(self, data, beginandend):
    #     num, Full_Name, case_description, result = data
    #     print(Full_Name,data)
    #     self.driver, self.logger = beginandend
    #     lp = LoginPage(self.driver)
    #     lp.login_echop(Full_Name)

    # 登录页面
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', 'Sheet2'))
    # def test_01(self, data, beginandend):
    #     num, username, password, case_description,result = data
    #     print(username, password, data)
    #     self.driver, self.logger = beginandend
    #     lp = LoginPage(self.driver)
    #     lp.login_test01(username, password)

    # 新增套餐
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增套餐用例'))
    # def test_add_package(self, data, beginandend):
    #     num, price, gives, description, text, give_num, result = data
    #     print(num, price, gives, description, text, give_num,data)
    #     self.driver, self.logger = beginandend
    #     pp = packagePage(self.driver)
    #     pp.addPackage(price, gives, description, text, give_num)

    # 修改套餐
    @pytest.mark.usefixtures('beginandend')
    @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增套餐用例'))
    def test_update_package(self, data, beginandend):
        num, price, gives, description, text, give_num, result = data
        print(num, price, gives, description, text, give_num, data)
        self.driver, self.logger = beginandend
        up = packagePage(self.driver)
        up.update_package(price, gives, description, text, give_num)

    # 删除套餐
    # @pytest.mark.usefixtures('beginandend')
    # def test_del_package(self, beginandend):
    #     self.driver, self.logger = beginandend
    #     dp = packagePage(self.driver)
    #     dp.delete_package()

    # 查询套餐
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '套餐查询用例'))
    # def test_query_package(self, data, beginandend):
    #     for i in range(len(data)):
    #         if data[i] is None:
    #             data[i] = 'null'
    #     num, Id, price, give_text, description, corner, num, give_num, result = data
    #     self.driver, self.logger = beginandend
    #     qp = packagePage(self.driver)
    #     qp.query_package(Id, price, give_text, description, corner, num, give_num)

    # 查询分组
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '套餐分组查询用例'))
    # def test_query_group(self, data,beginandend):
    #     for i in range(len(data)):
    #         if data[i] is None:
    #             data[i] = 'null'
    #     num, Id, title, type, result = data
    #     self.driver, self.logger = beginandend
    #     qg = packagePage(self.driver)
    #     qg.query_group(Id, title, type)

    # #删除分组
    # @pytest.mark.usefixtures("beginandend")
    # def test_del_grp(self, beginandend):
    #     self.driver, self.logger = beginandend
    #     dg = packagePage(self.driver)
    #     dg.del_group()


    # 新增分组
    # @pytest.mark.skip('新增分组')
    # @pytest.mark.usefixtures('beginandend')
    # @pytest.mark.parametrize("data", excle_read('./data/ele.xlsx', '新增套餐分组用例'))
    # def test_add_group(self, data, beginandend):
    #     num, title_name, result = data
    #     self.driver, self.logger = beginandend
    #     ad = packagePage(self.driver)
    #     ad.add_group(title_name)

        # 断言
        # if "登录成功" in case_description:
        #     # print(lp.get_except_result_access())
        #     assert lp.get_except_result_access() in result
        #     self.logger.info(case_description)
        # elif "登录失败" in case_description:
        #     # print(lp.get_except_result_fail())
        #     time.sleep(1)
        #     assert lp.get_except_result_fail() in result
        #     self.logger.info(case_description)






