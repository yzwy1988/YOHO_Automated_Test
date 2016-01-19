# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from Automan import PublicImp
from time import sleep

"""
   测试用例描述：Girls_热门品类左侧文字链接跳转, 选择商品加入购物车;
"""


def testcase_Web_CategoryFromGirl():

    PageImp.Page_HomeGuide.Page_HomeGuide.GoGirls.Click()

    PageImp.Page_Home.Page_Home.CategoryLink.ClickList()
    sleep(5)

    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()

    PublicImp.webelement.WebBrowser.Refresh()
    sleep(5)

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


