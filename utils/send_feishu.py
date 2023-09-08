# -*- coding: utf-8 -*-
"""
@Author : fmz
@Time : 2023/9/8 15:28
@File : send_feishu.py
"""
import base64
import hashlib
import hmac
import time

import requests


class Message:
    def get_sign(self, timestamp, secret):
        # 拼接timestamp和secret
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

    def feishu_message(self, summary=None):

        header = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        case_total = summary.get('total', 0)
        case_passed = summary.get('passed', 0)
        case_failed = summary.get('failed', 0)
        case_skipped = summary.get('skipped', 0)
        case_error = summary.get('error', 0)
        case_collected = summary.get('collected', 0)
        secret = 'wzWzbzCwkXRddT8JgXJNXg'

        timestamp = int(time.time())
        print(timestamp)

        sign = self.get_sign(timestamp, secret)
        print(sign)
        message_body = {
            "timestamp": timestamp,
            "msg_type": "text",
            "sign": sign,
            "content": {
                "text": f"<at user_id=\"all\">所有人</at> "
                f"执行用例的数量：{case_total}\n"
                f"收集到的用例：{case_collected}\n"
                f"pass用例数量：{case_passed}\n"
                f"failed用例数量：{case_failed}\n"
                f"skipped用例数量：{case_skipped}\n"
                f"error用例的数量：{case_error}"
            }
        }

        result = requests.post("https://open.feishu.cn/open-apis/bot/v2/hook/18ee99d0-a728-47c6-8f1e-9f8a57f28c68", headers=header, json=message_body)
        if result.status_code == 200:
            print("消息发送成功"+str(result.json()))
        else:
            print(f"消息发送失败，HTTP状态码: {result.status_code}")


if __name__ == '__main__':
    mes = Message()
    mes.feishu_message()