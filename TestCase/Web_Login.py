# -*- coding: utf-8 -*-

from Public import P_Login_out_web

"""
  有货手机App登录、退出
"""

def testcase_Login_And_Logout():
    P_Login_out_web.Login_and_out.Login()
    P_Login_out_web.Login_and_out.Logout()
