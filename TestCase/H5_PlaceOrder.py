# -*- coding: utf-8 -*-

from Public import P_Login_out_h5
from Page import PageImp
from Automan import PublicImp
from time import sleep


def testcase_H5_PlaceOrder():

    # 按power键点亮屏幕
    # PublicImp.env.driver.sendKeyEvent(26)

    PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.Click()

    """
    P_Login_out_h5.Login_And_out.login()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.headerYOHO.Click()
    # PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.Click()

    # 购物车列表--清空购物车
    PageImp.Page_Home.Page_Home.HeaderCart.Click()
    i = 0
    while i < 10:
        if PageImp.Page_ShopCart.Page_ShopCart.GiveawayImg.IsExist():
            PageImp.Page_ShopCart.Page_ShopCart.OrderListEM.ClickList_App()
            PageImp.Page_ShopCart.Page_ShopCart.DeleteFromOrder.Click()
        i += 1
    PageImp.Page_ShopCart.Page_ShopCart.ListBack.Click()
    """

    # 首页-点击新品到着
    PageImp.Page_Home.Page_Home.New.Click()

    # 新品到着列表--随机点击某商品图片
    PageImp.Page_GoodsList.Page_GoodsList.ToSelectOne.ClickList_App()

    # 添加商品到购物车--判断立即购买按钮是否存在,存在则点击;
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.ToBuyNow.IsExist():
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ToBuyNow.Click()
        sleep(3)
    else:
        # 若商品详情页不存在立即购买按钮,则返回至列表,重新点击商品进入商品详情页;
        PageImp.Page_GoodsDetails.Page_GoodsDetails.BackToList.Click()
        # 新品到着列表--随机点击某商品图片
        PageImp.Page_GoodsList.Page_GoodsList.ToSelectOne.ClickList_App()
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ToBuyNow.Click()
        sleep(3)

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
    if PageImp.Page_ConfirmOrder.Page_ConfirmOrder.GoBack.IsExist():
        PageImp.Page_ConfirmOrder.Page_ConfirmOrder.GoBack.Click()
    else:
        PublicImp.log.step_fail("Comfirm Order Is Fail!")
        # PublicImp.env.driver.execute_script('mobile: keyevent', {"keycode": "4"})
        # PublicImp.env.driver.keyevent(4)

    PageImp.Page_OrderDetails.Page_OrderDetails.ToPersonCenter.Click()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.MyOrders.Click()

    # 订单中心--取消订单
    if PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderListToSelect.IsExist():
        PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderListToSelect.Click()
        PageImp.Page_OrderDetails.Page_OrderDetails.Address.Click()
        PageImp.Page_OrderDetails.Page_OrderDetails.CancelOrder.Click()
    else:
        PublicImp.log.step_fail("Cancel Orser Is Fail!")

    P_Login_out_h5.Login_And_out.logout()
