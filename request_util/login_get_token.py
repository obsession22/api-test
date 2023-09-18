# -*- coding:utf-8 -*-

import requests


class Login_test:

    def get_token(self, url, json, headers):

        return requests.post(url, json=json, headers=headers)
