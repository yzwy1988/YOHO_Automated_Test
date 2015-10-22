# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from Automan import PublicImp
from time import sleep


def testcase_placeorder():
    """
      测试用例描述:
        访问网站--登录--点击导航栏购物车--进入购物车--清空购物车--返回首页--
        点击品牌一览--进入品牌列表页--点击快速导航中的N字母--点击NIKE品牌--进入nike商品列表页--
        选择列表中的第1个商品--点击进入商品详情页--选择颜色、尺码,点击添加到购物车--点击去购物车结算--
        进入购物车列表页--点击去结算--进入结算页面--选择收货地址,点击去付款,进入在线支付页面--
        点击导航栏中的订单中心--进入个人中心我的订单列表--选择刚下的订单--点击取消订单按钮--
        在弹出框内选择取消原因,点击确认按钮--完成订单取消操作--
        用户退出登录;
     """

    # 调用公共登录组件登录系统;
    P_Login_out_web.Login_and_out.Login()

    # 点击导航栏中 购物车 链接;
    # PageImp.Page_Home.Page_Home.ShopCart.MouseOver()
    # if PageImp.Page_Home.Page_Home.GoToCart.IsExist():
        # PageImp.Page_Home.Page_Home.GoToCart.Click()

    PublicImp.env.driver.get("http://www.yohobuy.com/shopping/cart")
    sleep(5)

    # 判断购物车列表中是否有商品,如果有则点击 批量删除 按钮清空购物车;
    if PageImp.Page_ShopCart.Page_ShopCart.ShopCartListSelectAll.IsExist():
        # PageImp.Page_ShopCart.Page_ShopCart.ShopCartListSelectAll.Click()
        # 购物车列表-批量删除
        # PageImp.Page_ShopCart.Page_ShopCart.ShopCartListBatchDelete.Click()
        # PublicImp.webelement.WebBrowser.AlertAccept()
        # 购物车列表-批量移入收藏夹
        PageImp.Page_ShopCart.Page_ShopCart.BatchAddToFavorites.Click()
        sleep(3)

    # 在购物车列表页面点击有货图标,进入网站首页;
    PageImp.Page_ShopCart.Page_ShopCart.GoToHome.Click()
    sleep(5)

    # 网站首页点击品牌一览,进入品牌列表页面
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    sleep(3)
    # 品牌列表页面,点击品牌快速导航中的N字母
    PageImp.Page_BrandList.Page_BrandList.brands_By_N.Click()
    sleep(3)
    # 点击Nike品牌,进入商品列表页面
    PageImp.Page_BrandList.Page_BrandList.Nike_brands.Click()
    sleep(5)

    # 商品列表--获取商品名称及商品价格
    # goodname = PageImp.Page_SearchResultList.Page_SearchResultList.GetGoodName.GetInnerHTML()
    # goodprice = PageImp.Page_SearchResultList.Page_SearchResultList.GetGoodPrice.GetInnerHTML()
    # print(goodname)
    # print(goodprice)

    # 商品列表页面,点击列表中商品,进入商品详情页面
    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()
    sleep(5)

    # 判断商品详情页面中的商品名称与商品价格与之前商品列表中选择的商品名称及价格信息是否一致
    # PageImp.Page_GoodsDetails.Page_GoodsDetails.Goods_Name.VerifyInnerHTMLContains(goodname)
    # PageImp.Page_GoodsDetails.Page_GoodsDetails.Goods_Price.VerifyInnerHTMLContains(goodprice)

    # 商品详情页面,选择颜色（未售罄）
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.GetObjectsCount() > 1:
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.ClickList()
    sleep(2)

    # 商品详情页面,选择尺码（未售罄）
    PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseSize.ClickList()
    sleep(2)

    # 商品详情页面,点击 添加到购物车按钮
    PageImp.Page_GoodsDetails.Page_GoodsDetails.BuyClickButton.Click()
    sleep(2)

    # 点击 去购物车结算 按钮,进入购物车列表页面
    PageImp.Page_GoodsDetails.Page_GoodsDetails.GotoCartButton.Click()
    sleep(5)

    # 购物车页面-选择赠品
    if PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng.IsExist():
        PageImp.Page_ShopCart.Page_ShopCart.Select_Mark_Zeng.Click()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Color.ClickList()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Size.ClickList()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_AddToCart.Click()
        sleep(5)

    # 购物车列表页面点击去结算按钮
    PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()
    sleep(5)

    # 结算页面--收货地址--判断是否有默认地址,如果有则跳过此步;如果没有则进入,先判断有没有地址,有则随机选择一个,没有则添加新地址;
    if PageImp.Page_OrderDetails.Page_OrderDetails.editAddress.IsExist():
        pass
    else:
        if PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.IsExist():
            PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.ClickList_App()
        else:
            PageImp.Page_OrderDetails.Page_OrderDetails.addressee_name.Set(unicode("测试"))
            PageImp.Page_OrderDetails.Page_OrderDetails.province.Select("上海市")
            PageImp.Page_OrderDetails.Page_OrderDetails.city.Select("上海市")
            PageImp.Page_OrderDetails.Page_OrderDetails.area_code.SelectByRandomOrder()
            PageImp.Page_OrderDetails.Page_OrderDetails.address.Set(unicode("经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
            PageImp.Page_OrderDetails.Page_OrderDetails.mobile.Set("13915992963")
            PageImp.Page_OrderDetails.Page_OrderDetails.email.Set("abc@126.com")
            PageImp.Page_OrderDetails.Page_OrderDetails.zip_code.Set("211100")
        PageImp.Page_OrderDetails.Page_OrderDetails.SaveShippingAddress.Click()
        sleep(2)

    # 结算页面--验证支付方式是否为"在线支付"
    if PageImp.Page_OrderDetails.Page_OrderDetails.PayMode.VerifyContentIsIncluded("在线支付"):
        pass
    else:
        # 结算页面--支付及送货时间--修改按钮
        PageImp.Page_OrderDetails.Page_OrderDetails.editPay.Click()
        # 结算页面--选择在线支付
        PageImp.Page_OrderDetails.Page_OrderDetails.pay_type1.Click()
        PageImp.Page_OrderDetails.Page_OrderDetails.PaymentButton.Click()

    # 结算页面,点击页面底部的 去付款 按钮,进入在线支付页面
    PageImp.Page_OrderDetails.Page_OrderDetails.ToPay.Click()

    # 在线支付页面--获取生成的订单编号
    ordernumber = PageImp.Page_OnlinePay.Page_OnlinePay.GetOrderNumber.GetInnerHTML()

    # 在线支付页面,点击页面顶部导航栏中 订单中心 链接,进入个人中心-我的订单列表;
    PageImp.Page_OnlinePay.Page_OnlinePay.GoToOrderCenter.Click()
    sleep(5)

    # 判断个人中心--我的订单列表中是否存在刚下单的订单号
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GetOrderNumber.VerifyInnerHTMLContains(ordernumber)

    # 个人中心-我的订单,选择刚下的订单,点击取消订单按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GetCancelOrderButton.Click()
    sleep(2)
    # 在弹出的选择取消原因页面,选择第2个原因
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GoToPopupAndSelect.Click()
    # 在弹出的选择取消原因页面,点击 确定并取消 订单按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_ClickIdentifyAndCancelOrder.Click()
    sleep(2)
    # 在成功取消订单提示内点击确定按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_ClickConfirm.Click()
    sleep(5)

    # 调用公共登录组件退出系统;
    P_Login_out_web.Login_and_out.Logout()
    sleep(3)
