# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Public_Imp
from Automan import PublicImp
from time import sleep

"""
   测试用例描述：Kids_优先品牌（大图）跳转, 选择商品加入购物车;
"""


def testcase_Web_AppropriateBrandFromKids():

    PageImp.Page_HomeGuide.Page_HomeGuide.GoKids.Click()

    href = PageImp.Page_Home.Page_Home.AppropriateBrandFromGirl.GetAttribute("href")

    PublicImp.env.driver.get(href)
    sleep(5)

    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()

    # 商品详情页面选择有库存商品加入购物车;
    P_Public_Imp.P_Web_GoodsDetails.P_Web_GoodsDetails.Web_GoodsDetails()

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


