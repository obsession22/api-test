# -*- coding:utf-8 -*-

from base.web_base import Base
from pageobject.login_page import Login


class UserInfo(Base):
    # 修改个人信息
    def update_user_info(self, logger, username, tel_number, mail_number, text):
        # 进入首页
        login =Login()
        login.login(logger)
        # 点击个人信息导航栏
        self.web_exe(__file__, 'login_click')
        # 输入昵称
        self.web_exe()
        # 输入手机号码
        self.web_exe()
        # 输入邮箱地址
        self.web_exe()
        # 输入个性签名
        self.web_exe()
        # 提交信息
        self.web_exe()

