"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@File : run_test.py
@Time : 2022/5/23 11:16
@Motto:Don't ever let somebody tell you you can't do something
"""

import os
import time
import pytest
import os
import zipfile
from utils.send_email import Mail

if __name__ == '__main__':

    pytest.main(['-vs', './TestCase', '--alluredir=./result', '--clean-alluredir'])

    # pytest.main(['-vs', './TestCase', '--alluredir=./result', '-n=5', '--reruns=2'])
    # split = 'allure' + ' generate' + ' ./report/result' + ' -o' + ' ./report/html' + ' --clean'
    time.sleep(1)
    # os.system('allure generate ./result -o ./report --clean')
    # os.system('allure open ./report ')

    os.system('allure serve ./result -o ./report --clean')



    mail = Mail()
    mail.send_qq_email()

# if __name__ == '__main__':
#     pytest.main()