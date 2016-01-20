# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Public_Imp
from Automan import PublicImp
from time import sleep

"""
   测试用例描述：Girls_热门品类右侧的图片链接跳转, 选择商品加入购物车;
"""


def testcase_Web_CategoryByPicFromGirl():

    PageImp.Page_HomeGuide.Page_HomeGuide.GoGirls.Click()

    PageImp.Page_Home.Page_Home.CategoryLinkByPic.ClickList()
    sleep(5)

    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()

    # 商品详情页面选择有库存商品加入购物车;
    P_Public_Imp.P_Web_GoodsDetails.P_Web_GoodsDetails.Web_GoodsDetails()

    # 调用公共模块:购物车列表,选择赠品/加价购
    P_Public_Imp.P_Web_ShopCart.P_Web_ShopCart.Web_ShopCartList()
