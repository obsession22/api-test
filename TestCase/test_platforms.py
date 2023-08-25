#!/usr/bin/env python
# -*-coding:utf-8 -*-
# -*- coding: utf-8 -*-
import time
import traceback

import allure
import pytest

from common.excle_export import excle_read

from pageobject.platforms_page import PlatformPage


@pytest.mark.usefixtures('beginandend')
@allure.feature('平台管理模块')
class Testplatforms:

    @pytest.mark.usefixtures('beginandend')
    @pytest.mark.parametrize('data',excle_read('./data/ele.xlsx', '推广链接查询用例'))
    def test_promotions(self, data, beginandend):
        for i in range(len(data)):
            if data[i] is None:
                data[i] = 'null'
                print(data[i])
        test_num, ID, vedio_id, episodes_id, user_id, set_id, pay_id, result = data
        self.driver, self.logger = beginandend
        p = PlatformPage(self.driver)
        p.query_promotions(ID, vedio_id, episodes_id, user_id, set_id, pay_id)


