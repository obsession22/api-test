# -*- coding:utf-8 -*-

import requests


class BaseApi:

    def base_get(self, url, headers=None, params=None):

       return requests.get(url, headers=headers, params=params)

    def base_post(self, url, headers=None, data=None, json=None):

       return requests.post(url,   json=json, data=data, headers=headers)

    def api(self, method, url, headers=None, data=None, params=None, json=None):

        if method == 'GET':
           return self.base_get(url, headers=headers, params=params)
        elif method == 'POST':
           return self.base_post(url, headers=headers, data=data, json=json)
        else:
            print('请输入"GET"或者"POST"')