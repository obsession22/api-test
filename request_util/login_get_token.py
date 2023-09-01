# -*- coding:utf-8 -*-

import requests
class Login_test:

    def get_token(self, url, json, headers):
       return requests.post(url, json=json, headers=headers)



# if __name__ == '__main__':
#
#     header = {'Accept':'application/json, text/plain, */*',
#              'Accept-Language':'zh_CN',
#              'Authorization': 'Bearer null',
#              'Origin': 'http://xctestadmin.xczxwe.com',
#              'Proxy-Connection': 'keep-alive',
#              'Referer': 'http://xctestadmin.xczxwe.com/',
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
#              'Content-Type': 'application/json;charset=UTF-8}'}
#     login = Login()
#     res = login.get_token(url='http://xctestadmin.xczxwe.com/prod/system/login',json={"username":"冯苗志","password":"123456"},headers = header).json()
#
#     print(res["data"]['token'])