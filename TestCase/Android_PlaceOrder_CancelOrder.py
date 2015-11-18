# -*- coding: utf-8 -*-

from Public import P_Login_out_android
from Page import PageImp
from Automan import PublicImp
from appium.webdriver.connectiontype import ConnectionType
from time import sleep
import datetime


def testcase_Android_PlaceOrder_CancelOrder():

    P_Login_out_android.Login_And_out.Login()

    PageImp.Page_Home.Page_Home.tabMain_my.Click()

    u""" 个人中心-我的订单-待付款-取消订单 """
    # PageImp.Page_PersonCenter.Page_PersonCenter.order_mine_dfk.Click()
    # PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.ClickList_App()
    # PageImp.Page_PersonCenter.Page_PersonCenter.order_dialog_confirm_btn.Click()
    # PageImp.Page_PersonCenter.Page_PersonCenter.order_back_imgbtn.Click()

    PageImp.Page_PersonCenter.Page_PersonCenter.order_mine_dfk.Click()

    if PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.IsExist():
        cancelcount = PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.GetObjectsCount()
        i = cancelcount
        while i > 0:
            PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.ClickList_App()
            PageImp.Page_PersonCenter.Page_PersonCenter.order_dialog_confirm_btn.Click()
            sleep(3)
            PublicImp.webelement.WebBrowser.swipeToDown(500)
            i = PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.GetObjectsCount()

    PageImp.Page_PersonCenter.Page_PersonCenter.order_back_imgbtn.Click()

    u""" 退出登录 """
    P_Login_out_android.Login_And_out.Logout()
