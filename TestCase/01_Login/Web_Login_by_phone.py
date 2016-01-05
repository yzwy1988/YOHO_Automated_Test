# -*- coding: utf-8 -*-

from Public import P_Login_out_web
from Page import PageImp
import time

"""
  测试用例描述：调用公共用例进行登录、退出--By Phone
"""


def web_login_by_mail():

    P_Login_out_web.Login_and_out.Login("15950554416", "123456")
    P_Login_out_web.Login_and_out.Logout()

