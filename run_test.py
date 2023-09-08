# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : run_test.py
@Time : 2022/5/23 11:16
@Motto:Don't ever let somebody tell you you can't do something
"""
import datetime
import time
import pytest
from pytest_jsonreport.plugin import JSONReport
import os
from utils.send_email import Mail
from utils.zip_util import zip_folder
from utils.send_feishu import Message

if __name__ == '__main__':
    plugin = JSONReport()
    data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pytest.main(['-vs', './TestCase', '--alluredir=./result', '--clean-alluredir'], plugins=[plugin])
    summary = plugin.report.get("summary")
    use_time = plugin.report.get("duration")
    print(summary)
    # print(str(plugin.report))
    time.sleep(1)
    # 生成allure报告
    os.system('allure generate ./result ')
    # os.system('allure open ./report ')
    # os.system('allure serve ./result -o ./report --clean')

    # 打包allure报告
    folder_to_zip = './report'  # 打包的文件路径
    zip_filename = 'test_report.zip'  # 打包后的文件名
    zip_folder(folder_to_zip, zip_filename)

    # 邮件发送
    mail = Mail()
    mail.send_qq_email(zip_filename, summary, use_time, data_time)

    # 飞书通知
    msg = Message()
    msg.feishu_message(summary)

    # 删除临时的zip文件
    os.remove(zip_filename)