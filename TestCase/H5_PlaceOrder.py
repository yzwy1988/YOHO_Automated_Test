# -*- coding: utf-8 -*-

from Public import P_Login_out_h5
from Page import PageImp
from Automan import PublicImp


def testcase_H5_PlaceOrder():

    P_Login_out_h5.Login_And_out.login()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.headerYOHO.Click()

    # P_Login_out_h5.Login_And_out.logout()
