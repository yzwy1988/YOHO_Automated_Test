# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from Automan import PublicImp
from time import sleep


def testcase_placeorder():
    """
      测试用例描述:
      使用货到付款、使用新地址、只双休日、节假日送货（工作时间不送货）、用顺丰速运，索要发票及备注信息、更改：送货前是否联系、是否打印价格
     """

    # 调用公共登录组件登录系统;
    P_Login_out_web.Login_and_out.Login()
    sleep(5)

    PublicImp.env.driver.get("http://www.yohobuy.com/shopping/cart")
    sleep(5)

    # 判断购物车列表中是否有商品,如果有则点击批量删除按钮清空购物车;
    if PageImp.Page_ShopCart.Page_ShopCart.ShopCartListSelectAll.IsExist():
        # PageImp.Page_ShopCart.Page_ShopCart.ShopCartListSelectAll.Click()
        PageImp.Page_ShopCart.Page_ShopCart.ShopCartListBatchDelete.Click()
        PublicImp.webelement.WebBrowser.AlertAccept()
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

    # 商品详情页面,选择尺码（未售罄）
    PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseSize.ClickList()
    sleep(2)

    # 商品详情页面,点击 添加到购物车按钮
    PageImp.Page_GoodsDetails.Page_GoodsDetails.BuyClickButton.Click()
    sleep(2)

    # 点击 去购物车结算 按钮,进入购物车列表页面
    PageImp.Page_GoodsDetails.Page_GoodsDetails.GotoCartButton.Click()
    sleep(5)

    # 购物车-选择赠品
    if PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng.IsExist():
        PageImp.Page_ShopCart.Page_ShopCart.Select_Mark_Zeng.Click()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Color.ClickList()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Size.ClickList()
        PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_AddToCart.Click()
        sleep(5)

    # 购物车列表页面点击去结算按钮
    PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()
    sleep(5)

    # 结算页面--收货地址--判断是否有默认地址,如果有则切换地址;
    if PageImp.Page_OrderDetails.Page_OrderDetails.NoSaveClose.IsExist():
        pass
    else:
        PageImp.Page_OrderDetails.Page_OrderDetails.editAddress.Click()

    # 判断结算页面-收货地址的总数,如果大于等于5,则随机删除一个地址
    if PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.IsExist():
        addresscount = PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.GetObjectsCount()
        if addresscount >= 5:
            PageImp.Page_OrderDetails.Page_OrderDetails.DelAddress.Click()
            sleep(3)

    # 结算页面--收货地址--使用新地址
    PageImp.Page_OrderDetails.Page_OrderDetails.AddNewAddess.Click()
    sleep(3)
    PageImp.Page_OrderDetails.Page_OrderDetails.addressee_name.Set(unicode("自动化测试"))
    PageImp.Page_OrderDetails.Page_OrderDetails.province.SelectByRandomOrder()
    PageImp.Page_OrderDetails.Page_OrderDetails.city.SelectByRandomOrder()
    PageImp.Page_OrderDetails.Page_OrderDetails.area_code.SelectByRandomOrder()
    PageImp.Page_OrderDetails.Page_OrderDetails.address.Set(unicode("经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
    PageImp.Page_OrderDetails.Page_OrderDetails.mobile.Set("13915992963")
    PageImp.Page_OrderDetails.Page_OrderDetails.email.Set("abc@126.com")
    PageImp.Page_OrderDetails.Page_OrderDetails.zip_code.Set("211100")
    # 结算页面--收货地址--保存并送到这个地址
    PageImp.Page_OrderDetails.Page_OrderDetails.SaveShippingAddress.Click()

    # 结算页面--支付及送货时间--修改按钮
    PageImp.Page_OrderDetails.Page_OrderDetails.editPay.Click()
    # 结算页面--选择货到付款
    PageImp.Page_OrderDetails.Page_OrderDetails.pay_type2.Click()
    # 结算页面--选择支付及送货时间
    PageImp.Page_OrderDetails.Page_OrderDetails.SelectDeliverTime.ClickList_App()
    PageImp.Page_OrderDetails.Page_OrderDetails.ContactBeforeDelivery.ClickList_App()
    PageImp.Page_OrderDetails.Page_OrderDetails.PaymentButton.Click()
    # 结算页面--验证支付方式是否为"货到付款"
    PageImp.Page_OrderDetails.Page_OrderDetails.PayMode.VerifyInnerHTMLContains("货到付款")
    sleep(3)

    # 结算页面--选择快递
    if PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_shunfeng.IsExist():
        PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_shunfeng.Click()

    # 结算页面--索要发票、添加备注信息
    PageImp.Page_OrderDetails.Page_OrderDetails.ShowInvoices.Click()
    PageImp.Page_OrderDetails.Page_OrderDetails.InvoicesPayable.Set(unicode("YOHO"))
    PageImp.Page_OrderDetails.Page_OrderDetails.invoicesType.SelectByRandomOrder()
    PageImp.Page_OrderDetails.Page_OrderDetails.ShowRemark.Click()
    PageImp.Page_OrderDetails.Page_OrderDetails.Remark.Set(unicode("YOHO备注信息"))
    PageImp.Page_OrderDetails.Page_OrderDetails.RemarkBox.ClickList_App()

    # 结算页面,点击页面底部的 去付款 按钮,进入在线支付页面
    PageImp.Page_OrderDetails.Page_OrderDetails.ToPay.Click()

    # 订单成页面(货到付款)--获取订单号
    ordernumber = PageImp.OrderSuccessPage.OrderSuccessPage.GetOrderNumber.GetInnerHTML()
    # 订单成页面(货到付款)--点击页面顶部导航栏中的订单中心链接,进入个人中心-我的订单;
    PageImp.OrderSuccessPage.OrderSuccessPage.GoToOrderCenter.Click()
    sleep(5)

    # 判断个人中心--我的订单列表中是否存在刚下单的订单号
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GetOrderNumber.VerifyInnerHTMLContains(ordernumber)

    # 个人中心-我的订单,选择刚下的订单,点击取消订单按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GetCancelOrderButton.Click()
    sleep(3)
    # 在弹出的选择取消原因页面,选择第2个原因
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_GoToPopupAndSelect.Click()
    # 在弹出的选择取消原因页面,点击 确定并取消 订单按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_ClickIdentifyAndCancelOrder.Click()
    sleep(2)
    # 在成功取消订单提示内点击确定按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.OrderCenter_ClickConfirm.Click()
    sleep(3)

    # 调用公共登录组件退出系统;
    P_Login_out_web.Login_and_out.Logout()
    sleep(3)
