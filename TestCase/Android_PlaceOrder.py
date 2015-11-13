# -*- coding: utf-8 -*-

from Public import P_Login_out_android
from Page import PageImp
from Automan import PublicImp
from appium.webdriver.connectiontype import ConnectionType
from time import sleep
import datetime


def testcase_Android_PlaceOrder():

    # 设置网络连接情况
    # PublicImp.env.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
    # PublicImp.env.driver.set_network_connection(ConnectionType.WIFI_ONLY)

    P_Login_out_android.Login_And_out.Login()

    PageImp.Page_Home.Page_Home.tabMain_shoppCard.Click()

    u""" 购物车列表-判断购物车列表是否有商品-如若有商品,点击全选进行删除-开始 """
    if PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_Select_All.IsExist():
        checked_value = PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_Select_All.GetAttribute("checked")
        if checked_value == "true":
            PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_Select_All.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_Select_All.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_right_btn.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_delete_btn.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_delete_confirm.Click()
    u""" 购物车列表-判断购物车列表是否有商品-如若有商品,点击全选进行删除-结束 """

    PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_back_imgbtn.Click()

    PageImp.Page_Home.Page_Home.tabMain_home.Click()
    PageImp.Page_Home.Page_Home.New.Click()

    u""" 首页-点击新品-进入新品列表-若加载失败-返回首页-重新再次点击新品 """
    if PageImp.Page_Home.Page_Home.loading_failure_btn.IsExist():
        PageImp.Page_Home.Page_Home.back_imgbtn.Click()
        PageImp.Page_Home.Page_Home.New.Click()

    u""" 获取移动设备的分辨率：宽和高 """
    width = PublicImp.env.driver.get_window_size()['width']
    height = PublicImp.env.driver.get_window_size()['height']
    X_width = width/2
    Y_height = height - 200

    # PublicImp.env.driver.switch_to.context("NATIVE_APP")
    # PublicImp.env.driver.swipe(X_width, Y_height, X_width, 200)

    PublicImp.webelement.WebBrowser.swipeToUp(500)
    sleep(2)
    PublicImp.webelement.WebBrowser.swipeToUp(500)

    PageImp.Page_Home.Page_Home.New_Products.ClickList_App()
    sleep(5)

    if PageImp.Page_Product_Detail.Page_Product_Detail.product_detail_add.IsExist():
        pass
    elif PageImp.Page_Home.Page_Home.New_Products.IsExist():
        PublicImp.webelement.WebBrowser.swipeToUp(500)
        PageImp.Page_Home.Page_Home.New_Products.ClickList_App()
        sleep(5)
    else:
        PageImp.Page_Product_Detail.Page_Product_Detail.back_imgbtn.Click()
        PageImp.Page_Home.Page_Home.New_Products.ClickList_App()
        sleep(5)
    PageImp.Page_Product_Detail.Page_Product_Detail.product_detail_add.Click()

    u""" 商品详情页-尺码、颜色选择页面-随机选择有库存的颜色、尺码-开始 """
    i = 0
    while i < 10:
        if PageImp.Page_Product_Detail.Page_Product_Detail.product_size.GetObjectsCount() > 1:
            PageImp.Page_Product_Detail.Page_Product_Detail.product_color.ClickList_App()
            PageImp.Page_Product_Detail.Page_Product_Detail.product_size.ClickList_App()
        elif PageImp.Page_Product_Detail.Page_Product_Detail.product_color.GetObjectsCount() > 1:
            PageImp.Page_Product_Detail.Page_Product_Detail.product_color.ClickList_App()
            PageImp.Page_Product_Detail.Page_Product_Detail.product_size.ClickList_App()

        PublicImp.webelement.WebBrowser.swipeToUp(500)
        pro_num = PageImp.Page_Product_Detail.Page_Product_Detail.tv_pro_info_num.GetAttribute("text")
        if pro_num != "0":
            PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
            sleep(5)
            if PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.IsExist():
                continue
            else:
                break
        else:
            continue
    u""" 商品详情页-尺码、颜色选择页面-随机选择有库存的颜色、尺码-结束 """

    # PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
    # sleep(5)
    PageImp.Page_Product_Detail.Page_Product_Detail.shop_cart.Click()

    u""" 购物车列表-选择赠品-开始 """
    if PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift.IsExist():
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift_goods_image.ClickList_App()

        i = 0
        while i <= 5:
            PageImp.Page_Product_Detail.Page_Product_Detail.product_color.ClickList_App()
            PageImp.Page_Product_Detail.Page_Product_Detail.product_size.ClickList_App()
            PublicImp.webelement.WebBrowser.swipeToUp(500)
            pro_num = PageImp.Page_Product_Detail.Page_Product_Detail.tv_pro_info_num.GetAttribute("text")
            if pro_num != 0:
                PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
                sleep(5)
                if PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.IsExist():
                    continue
                else:
                    break

        # PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
    u""" 购物车列表-选择赠品-结束 """

    u""" 购物车列表-选择加价购-开始 """
    u""" 购物车列表-选择加价购-结束 """

    PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_jiesuan_btn.Click()

    u""" 购物车列表-收货地址--开始 """
    # 收货地址列表--如果有数据,随机点击选择一个,若没有,则添加新地址;
    if PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_Address.IsExist():
        PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_Address.Click()
    else:
        sleep(5)
        PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_Address.Click()

    addresscount = PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.GetObjectsCount()
    if addresscount > 0:
        # 随机选择一个收货地址;
        # PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.ClickList_App()
        while addresscount >= 5:
            # 收货地址列表数据大于等于5个情况下
            PageImp.Page_Confirm_Order.Page_Confirm_Order.address_manager.Click()
            PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.LongClickList_App()
            PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmButton.Click()
            PageImp.Page_Confirm_Order.Page_Confirm_Order.backbtn.Click()
            addresscount = PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.GetObjectsCount()

        PageImp.Page_Confirm_Order.Page_Confirm_Order.AddNewAdress.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.name.Set(unicode("测试_%s" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
        PageImp.Page_Confirm_Order.Page_Confirm_Order.mobile.Set("13915992963")
        PageImp.Page_Confirm_Order.Page_Confirm_Order.area.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.addressdetail.Set(unicode("江宁经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
        sleep(3)
        PageImp.Page_Confirm_Order.Page_Confirm_Order.editAndsave.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.ClickList_App()
    else:
        # 地址列表无数据情况下,添加新地址;
        PageImp.Page_Confirm_Order.Page_Confirm_Order.AddAddressTitle.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.name.Set(unicode("测试_%s" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
        PageImp.Page_Confirm_Order.Page_Confirm_Order.mobile.Set("13915992963")
        PageImp.Page_Confirm_Order.Page_Confirm_Order.area.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.SelectArea.ClickList_App()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.addressdetail.Set(unicode("江宁经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
        sleep(3)
        PageImp.Page_Confirm_Order.Page_Confirm_Order.editAndsave.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.AddressList_addressname.ClickList_App()
    u""" 购物车列表-收货地址--结束 """

    u""" 购物车列表-支付方式-开始 """
    PageImp.Page_Confirm_Order.Page_Confirm_Order.payway.Click()
    # 支付方式--在线支付(推荐)
    PageImp.Page_Confirm_Order.Page_Confirm_Order.OnlinePayment.Click()
    # 支付方式--货到付款
    # PageImp.Page_Confirm_Order.Page_Confirm_Order.COD.Click()

    u""" 购物车列表-配送方式-开始 """
    PageImp.Page_Confirm_Order.Page_Confirm_Order.deliveryway.Click()
    # 配送方式--普通快递
    # PageImp.Page_Confirm_Order.Page_Confirm_Order.NormalDelivery.Click()
    # 配送方式--顺丰速运
    PageImp.Page_Confirm_Order.Page_Confirm_Order.ExpressDelivery.Click()
    # 配送方式--如果不支付顺丰速运--弹出提示框--点击确定按钮;
    if PageImp.Page_Confirm_Order.Page_Confirm_Order.dialog_message.IsExist():
        PageImp.Page_Confirm_Order.Page_Confirm_Order.dialog_ok.Click()

    u""" 购物车列表-送货时间-开始 """
    PageImp.Page_Confirm_Order.Page_Confirm_Order.send_time.Click()
    # 送货时间--随机选择一个送货时间;
    PageImp.Page_Confirm_Order.Page_Confirm_Order.send_time_3.Click()

    u""" 确定订单页-向上滑动 """
    PublicImp.webelement.WebBrowser.swipeToUp(500)
    sleep(2)

    u""" 结算页面--发票/备注 """
    PageImp.Page_Confirm_Order.Page_Confirm_Order.receipt_toggle.Click()

    u""" 确定订单页-向上滑动 """
    PublicImp.webelement.WebBrowser.swipeToUp(500)
    sleep(2)

    PageImp.Page_Confirm_Order.Page_Confirm_Order.invoices_title.Set(unicode("发票抬头--测试"))
    sleep(2)
    PageImp.Page_Confirm_Order.Page_Confirm_Order.receipt_type.Click()
    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": X_width, "y": height-300})
    sleep(2)
    PageImp.Page_Confirm_Order.Page_Confirm_Order.remark.Set(unicode("备注--测试"))
    sleep(2)

    u"""
    js_snippet = "mobile: swipe"
    args = {'startX': 100, 'startY': 500, 'endX': 100, 'endY': 50, 'tapCount': 1, 'duration': 500}
    PublicImp.env.driver.execute_script(js_snippet, args)
    """

    PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_make_sure_order.Click()
    sleep(5)

    if PageImp.Page_Confirm_Order.Page_Confirm_Order.dialog_message.IsExist():
        PageImp.Page_Confirm_Order.Page_Confirm_Order.dialog_ok.Click()
        PublicImp.webelement.WebBrowser.swipeToDown(500)
        PageImp.Page_Confirm_Order.Page_Confirm_Order.deliveryway.Click()
        PageImp.Page_Confirm_Order.Page_Confirm_Order.NormalDelivery.Click()
        PublicImp.webelement.WebBrowser.swipeToUp(500)
        PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_make_sure_order.Click()
        sleep(5)

    if PageImp.OrderSuccessPage.OrderSuccessPage.showorder.IsExist():
        # 如果是货到付款,则执行如下操作;
        PageImp.OrderSuccessPage.OrderSuccessPage.goanywhereBtn.Click()
        PageImp.Page_Home.Page_Home.back_imgbtn.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_back_imgbtn.Click()
        PageImp.Page_Product_Detail.Page_Product_Detail.back_imgbtn.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_back_imgbtn.Click()
    else:
        # 如果是在线支付,则执行如下操作;
        PageImp.Page_Confirm_Order.Page_Confirm_Order.actionBar_backBtn.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_back_imgbtn.Click()
        PageImp.Page_Product_Detail.Page_Product_Detail.back_imgbtn.Click()
        PageImp.Page_Home.Page_Home.back_imgbtn.Click()

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
