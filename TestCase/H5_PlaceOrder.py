# -*- coding: utf-8 -*-

from Public import P_Login_out_h5
from Page import PageImp
from Automan import PublicImp
from time import sleep


def testcase_H5_PlaceOrder():

    # 唤醒屏幕
    # PublicImp.env.driver.keyevent(26)

    PublicImp.webelement.WebBrowser.Refresh()
    sleep(2)

    if PageImp.Page_HomeGuide.Page_HomeGuide.Float_Layer_Close.IsExist():
        # Mate7
        # PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 20, "y": 1640})
        # ZTE U5S
        PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 15, "y": 1165})

    PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.Click()

    PageImp.Page_Home.Page_Home.footer_tab_main.Click()

    P_Login_out_h5.Login_And_out.login()

    PageImp.Page_PersonalCenter.Page_PersonalCenter.GoToHome.Click()

    # 购物车列表--清空购物车
    PageImp.Page_Home.Page_Home.footer_tab_shopcart.Click()

    if PageImp.Page_ShopCart.Page_ShopCart.GiveawayImg.IsExist():
        goodcount = PageImp.Page_ShopCart.Page_ShopCart.GiveawayImg.GetObjectsCount()
        i = goodcount
        while i > 0:
            # PageImp.Page_ShopCart.Page_ShopCart.OrderListEM.ClickList_App()
            # PageImp.Page_ShopCart.Page_ShopCart.EnsureDel.Click()
            PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 664, "y": 455})
            PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 500, "y": 800})
            sleep(3)
            i = PageImp.Page_ShopCart.Page_ShopCart.GiveawayImg.GetObjectsCount()

        PageImp.Page_ShopCart.Page_ShopCart.JustLook.Click()
        PageImp.Page_GoodsList.Page_GoodsList.GoToHome.Click()
    else:
        PublicImp.webelement.WebBrowser.Refresh()
        sleep(2)
        PageImp.Page_ShopCart.Page_ShopCart.ListBack.Click()

    # 首页-点击新品到着
    PageImp.Page_Home.Page_Home.New.Click()
    PublicImp.webelement.WebBrowser.Refresh()

    # 新品到着列表--随机点击某商品图片
    PageImp.Page_GoodsList.Page_GoodsList.ToSelectOne.ClickList_App()
    PublicImp.webelement.WebBrowser.Refresh()

    u"""
    # 添加商品到购物车--判断立即购买按钮是否存在,存在则点击;
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.addCartButton.IsExist():
        PageImp.Page_GoodsDetails.Page_GoodsDetails.addCartButton.Click()
        sleep(3)
    else:
        # 若商品详情页不存在立即购买按钮,则返回至列表,重新点击商品进入商品详情页;
        PageImp.Page_GoodsDetails.Page_GoodsDetails.BackToList.Click()
        # 新品到着列表--随机点击某商品图片
        PageImp.Page_GoodsList.Page_GoodsList.ToSelectOne.ClickList_App()
        PageImp.Page_GoodsDetails.Page_GoodsDetails.addCartButton.Click()

    PageImp.Page_GoodsDetails.Page_GoodsDetails.AddCartChooseColor.ClickList_App()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.AddCartSizeList.ClickList_App()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.addCartButton2.Click()
    """

    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 333, "y": 1200})
    sleep(2)
    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 170, "y": 870})
    sleep(2)
    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 170, "y": 970})
    sleep(2)
    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 360, "y": 1220})
    sleep(2)

    PageImp.Page_GoodsDetails.Page_GoodsDetails.ShopCartIcon.Click()

    PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 613, "y": 1213})
    sleep(2)

    # 购物车列表--点击结算按钮
    # PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()
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

    PageImp.Page_OrderList.Page_OrderList.GoToHome.Click()
    PageImp.Page_Home.Page_Home.footer_tab_main.Click()
    PageImp.Page_PersonalCenter.Page_PersonalCenter.ToPayOrder.Click()

    # 订单中心--取消订单
    if PageImp.Page_OrderList.Page_OrderList.GoodImgs.IsExist():
        GoodImgscount = PageImp.Page_OrderList.Page_OrderList.GoodImgs.GetObjectsCount()
        i = GoodImgscount
        while i > 0:
            # PublicImp.webelement.WebBrowser.Refresh()
            # 进入订单详情页面进行取消订单
            # PageImp.Page_OrderList.Page_OrderList.GoodImgs.Click()
            # PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 100, "y": 560})
            # PageImp.Page_OrderDetails.Page_OrderDetails.Address.Click()
            # PageImp.Page_OrderDetails.Page_OrderDetails.CancelOrder.Click()
            # PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 500, "y": 800})
            # PageImp.Page_OrderDetails.Page_OrderDetails.BackToOrderList.Click()
            # 订单列表直接点击取消订单按钮;
            # PageImp.Page_OrderList.Page_OrderList.CancelOrder.Click()
            PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 410, "y": 910})
            sleep(2)
            PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 500, "y": 800})
            sleep(2)
            PageImp.Page_OrderList.Page_OrderList.ForPayButton.Click()
            # PageImp.Page_OrderList.Page_OrderList.ConfirmButton.Click()
            # PublicImp.env.driver.execute_script("mobile: tap", {"touchCount": "1", "x": 500, "y": 810})
            # PublicImp.webelement.WebBrowser.Refresh()
            i = PageImp.Page_OrderList.Page_OrderList.GoodImgs.GetObjectsCount()

    PageImp.Page_OrderList.Page_OrderList.BackToPersonCenter.Click()

    P_Login_out_h5.Login_And_out.logout()
