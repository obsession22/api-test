# -*- coding:utf-8 -*-

import requests


class BaseApi:

    def base_get(self, url, header=None, params=None):

        requests.get(url, header=header, params=params)

    def base_post(self, url, header=None, data=None, json=None):

        requests.post(url, header=header, data=data, json=json)

    def api(self, method, url, header=None, params=None, data=None, json=None):
        if method =='GET':
            self.base_get(url, header=header, params=params)
        elif method == 'POST':
            self.base_post(url, header=header, data=data, json=json)
        else:
            print('请输入"GET"或者"POST"')