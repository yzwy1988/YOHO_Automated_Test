# -*- coding: utf-8 -*-

from Public import P_Login_out_h5
from Page import PageImp
from Automan import PublicImp


def testcase_H5_PlaceOrder():

    P_Login_out_h5.Login_And_out.login()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.headerYOHO.Click()

    # 购物车列表--清空购物车
    PageImp.Page_Home.Page_Home.HeaderCart.Click()
    i = 0
    while i < 10:
        if PageImp.Page_ShopCart.Page_ShopCart.GiveawayImg.IsExist():
            PageImp.Page_ShopCart.Page_ShopCart.OrderListEM.ClickList_App()
            PageImp.Page_ShopCart.Page_ShopCart.DeleteFromOrder.Click()
        i += 1
    PageImp.Page_ShopCart.Page_ShopCart.ListBack.Click()

    # 首页-点击新品到着
    PageImp.Page_Home.Page_Home.New.Click()

    # 新品到着列表--随机点击某商品图片
    PageImp.Page_GoodsList.Page_GoodsList.ToSelectOne.ClickList_App()

    # 添加商品到购物车
    PageImp.Page_GoodsDetails.Page_GoodsDetails.ToBuyNow.Click()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.AddCartChooseColor.ClickList_App()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.AddCartSizeList.ClickList_App()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.addCartButton.Click()

    # 购物车列表--点击结算按钮
    PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()

    # 确认订单--随机选择送货时间
    PageImp.Page_ConfirmOrder.Page_ConfirmOrder.DeliveryWay.ClickList_App()

    # 确认订单--随机选择送货时间
    PageImp.Page_ConfirmOrder.Page_ConfirmOrder.DeliveryTime.ClickList_App()

    # 确认订单--选择支付方式--支付宝支付
    PageImp.Page_ConfirmOrder.Page_ConfirmOrder.PayByZhifubao.Click()

    # 订单成功页面
    PageImp.Page_ConfirmOrder.Page_ConfirmOrder.GoBack.Click()

    PageImp.Page_OrderDetails.Page_OrderDetails.ToPersonCenter.Click()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.MyOrders.Click()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderListToSelect.Click()

    # swipe_args = {'startX': 0.5, 'startY': 0.5, 'endX': 0.5, 'endY': 0.1, 'duration': 10}
    # PublicImp.env.driver.execute_script("mobile: swipe", swipe_args)

    PageImp.Page_OrderDetails.Page_OrderDetails.Address.Click()

    PageImp.Page_OrderDetails.Page_OrderDetails.CancelOrder.Click()

    P_Login_out_h5.Login_And_out.logout()
