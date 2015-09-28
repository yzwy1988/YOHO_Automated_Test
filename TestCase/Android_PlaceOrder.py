# -*- coding: utf-8 -*-

from Public import P_Login_out_android
from Page import PageImp
from Automan import PublicImp


def testcase_Android_PlaceOrder():

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

    PublicImp.env.driver.switch_to.context("NATIVE_APP")
    PublicImp.env.driver.swipe(X_width, Y_height, X_width, 200)

    PageImp.Page_Home.Page_Home.New_Products.ClickList_App()
    PageImp.Page_Product_Detail.Page_Product_Detail.product_detail_add.Click()

    u""" 商品详情页-尺码、颜色选择页面-随机选择有库存的颜色、尺码-开始 """
    i = 0
    while i < 5:
        PageImp.Page_Product_Detail.Page_Product_Detail.product_color.ClickList_App()
        PageImp.Page_Product_Detail.Page_Product_Detail.product_size.ClickList_App()
        PublicImp.env.driver.switch_to.context("NATIVE_APP")
        PublicImp.env.driver.swipe(X_width, Y_height, X_width, 200)
        pro_num = PageImp.Page_Product_Detail.Page_Product_Detail.tv_pro_info_num.GetAttribute("text")
        if pro_num != 0:
            break
        else:
            continue
    u""" 商品详情页-尺码、颜色选择页面-随机选择有库存的颜色、尺码-结束 """

    PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
    PageImp.Page_Product_Detail.Page_Product_Detail.shop_cart.Click()

    u""" 购物车列表-选择赠品-开始 """
    if PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift.IsExist():
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift.Click()
        PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_gift_goods_image.Click()

        i = 0
        while i <= 5:
            PageImp.Page_Product_Detail.Page_Product_Detail.product_color.ClickList_App()
            PageImp.Page_Product_Detail.Page_Product_Detail.product_size.ClickList_App()
            PublicImp.env.driver.switch_to.context("NATIVE_APP")
            PublicImp.env.driver.swipe(X_width, Y_height, X_width, 200)
            pro_num = PageImp.Page_Product_Detail.Page_Product_Detail.tv_pro_info_num.GetAttribute("text")
            if pro_num != 0:
                break

        PageImp.Page_Product_Detail.Page_Product_Detail.pro_info_submit.Click()
    u""" 购物车列表-选择赠品-结束 """

    PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_jiesuan_btn.Click()

    u"""
    js_snippet = "mobile: swipe"
    args = {'startX': 100, 'startY': 500, 'endX': 100, 'endY': 50, 'tapCount': 1, 'duration': 500}
    PublicImp.env.driver.execute_script(js_snippet, args)
    """

    u""" 确定订单页-向上滑动 """
    PublicImp.env.driver.switch_to.context("NATIVE_APP")
    PublicImp.env.driver.swipe(X_width, Y_height, X_width, 200)

    PageImp.Page_Confirm_Order.Page_Confirm_Order.ConfirmOrder_make_sure_order.Click()
    PageImp.Page_Confirm_Order.Page_Confirm_Order.actionBar_backBtn.Click()

    PageImp.Page_Shop_Cart.Page_Shop_Cart.shoppingcart_back_imgbtn.Click()
    PageImp.Page_Product_Detail.Page_Product_Detail.back_imgbtn.Click()
    PageImp.Page_Home.Page_Home.back_imgbtn.Click()
    PageImp.Page_Home.Page_Home.tabMain_my.Click()

    u""" 个人中心-我的订单-待付款-取消订单 """
    PageImp.Page_PersonCenter.Page_PersonCenter.order_mine_dfk.Click()
    PageImp.Page_PersonCenter.Page_PersonCenter.order_item_cancel_btn.ClickList_App()
    PageImp.Page_PersonCenter.Page_PersonCenter.order_dialog_confirm_btn.Click()
    PageImp.Page_PersonCenter.Page_PersonCenter.order_back_imgbtn.Click()

    u""" 退出登录 """
    P_Login_out_android.Login_And_out.Logout()
