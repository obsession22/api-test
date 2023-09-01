#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import sys
import time

from base.web_base import Base
from request_util.login_get_token import Login_test
class Login(Base):
    def login(self, logger):
        header = {'Accept': 'application/json, text/plain, */*',
                  'Accept-Language': 'zh_CN',
                  'Authorization': 'Bearer null',
                  'Origin': 'http://xctestadmin.xczxwe.com',
                  'Proxy-Connection': 'keep-alive',
                  'Referer': 'http://xctestadmin.xczxwe.com/',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                  'Content-Type': 'application/json;charset=UTF-8}'}
        login = Login_test()
        res = login.get_token(url='http://xctestadmin.xczxwe.com/prod/system/login',json={"username": "冯苗志", "password":"123456"}, headers=header).json()
        token = res['data']['token']
        print(token)
        token_value = f'"{token}"'
        # print(token_value)
        self.driver.get('http://xctestadmin.xczxwe.com')
        script = f"localStorage.setItem('token', '{token_value}')"
        self.driver.execute_script(script)
        self.driver.get('http://xctestadmin.xczxwe.com')
        time.sleep(2)
        # print(token_value)



