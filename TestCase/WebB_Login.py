# -*- coding: utf-8 -*-

from Public import P_Login_out_web
from Page import PageImp
import time


def testcase_Login_And_Logout():

    P_Login_out_web.Login_and_out.Login()

    for i in xrange(30):
        PageImp.Page_Home.Page_Home.ShopCart.movetoelement()
        PageImp.Page_Home.Page_Home.miniCartBoxNumber.Click()
        if PageImp.Page_Home.Page_Home.GoToCart.IsExist():
            PageImp.Page_Home.Page_Home.GoToCart.Click()
            time.sleep(5)
            break
