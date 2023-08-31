#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import time

from base.web_base import Base


class Login(Base):
    def login(self, logger, text):

        self.load("https://www.baidu.com/")
        time.sleep(2)
        self.web_exe(__file__, 'login_input', text=text)
        time.sleep(2)
        self.web_exe(__file__, 'login_click')
        time.sleep(2)


