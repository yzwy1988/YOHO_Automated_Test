# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from Automan import PublicImp
from time import sleep

"""
   测试用例描述：男生频道--从list品类页面选择商品加入购物车;
"""


def testcase_Web_AddToCartFromList_LS():

    PageImp.Page_HomeGuide.Page_HomeGuide.GoLifeStyle.Click()

    # PageImp.Page_Home.Page_Home.ListNameFuShi.Click()
    PublicImp.env.driver.get("http://list.yohobuy.com/?msort=10&misort=103")
    sleep(5)

    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()

    PublicImp.webelement.WebBrowser.Refresh()
    sleep(3)

    # 商品详情页面,选择颜色（未售罄）
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.GetObjectsCount() > 1:
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.ClickList()
    sleep(2)

    # 商品详情页面,选择尺码（未售罄）
    PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseSize.ClickList()
    sleep(2)

    # 商品详情页面,点击 添加到购物车按钮
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.BuyClickButton.IsExist():
        pass
    else:
        sleep(10)
    PageImp.Page_GoodsDetails.Page_GoodsDetails.BuyClickButton.Click()
    sleep(3)

    # 点击 去购物车结算 按钮,进入购物车列表页面
    PageImp.Page_GoodsDetails.Page_GoodsDetails.GotoCartButton.Click()
    sleep(5)

    # 购物车列表页面点击去结算按钮
    PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()
    sleep(5)

