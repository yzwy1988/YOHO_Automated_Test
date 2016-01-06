# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from Automan import PublicImp
from time import sleep

"""
测试用例描述:
    登录--清空购物车--选择商品加入购物车--点击列表中的移入收藏夹--进入个人中心--我的收藏--验证移入收藏夹是否成功;
"""


def testcase_placeorder_5():

    # 调用公共登录组件登录系统;
    P_Login_out_web.Login_and_out.Login()
    sleep(5)

    PublicImp.env.driver.get("http://www.yohobuy.com/shopping/cart")
    sleep(5)

    # 判断购物车列表中是否有商品,如果有则点击批量删除按钮清空购物车;
    if PageImp.Page_ShopCart.Page_ShopCart.ShopCartListSelectAll.IsExist():
        PageImp.Page_ShopCart.Page_ShopCart.ShopCartListBatchDelete.Click()
        PublicImp.webelement.WebBrowser.AlertAccept()
        sleep(3)

    # 在购物车列表页面点击有货图标,进入网站首页;
    PageImp.Page_ShopCart.Page_ShopCart.GoToHome.Click()
    sleep(5)

    # 网站首页点击品牌一览,进入品牌列表页面
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    sleep(3)

    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    # 品牌列表页面,点击品牌快速导航中的N字母
    # PageImp.Page_BrandList.Page_BrandList.brands_By_N.Click()
    # sleep(3)
    # 点击Nike品牌,进入商品列表页面
    # PageImp.Page_BrandList.Page_BrandList.Nike_brands.Click()
    sleep(5)

    # 商品列表页面,点击列表中商品,进入商品详情页面
    PageImp.Page_SearchResultList.Page_SearchResultList.ResultList.ClickList()
    sleep(5)

    PublicImp.webelement.WebBrowser.Refresh()
    sleep(5)

    # 商品详情页面,选择颜色（未售罄）
    if PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.GetObjectsCount() > 1:
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.ClickList()

    # 商品详情页面,选择尺码（未售罄）
    PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseSize.ClickList()
    sleep(2)

    goodname = PageImp.Page_GoodsDetails.Page_GoodsDetails.Goods_Name.GetInnerHTML()

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

    PublicImp.webelement.WebBrowser.Refresh()
    sleep(5)

    # 购物车页面--列表--选择商品点击移入收藏夹
    PageImp.Page_ShopCart.Page_ShopCart.AddToFavorites.ClickList_App()
    sleep(3)

    # 购物车页面--空列表--点击查看订单按钮
    PageImp.Page_ShopCart.Page_ShopCart.ViewOrdersLink.Click()

    # 个人中心--左侧菜单--我的收藏
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_MyFavorite.Click()

    # 个人中心--我的收藏--验证收藏是否正确;
    personcentergoodname = PageImp.Page_PersonalCenter.Page_PersonalCenter.GetGoodName.GetInnerHTML()
    if personcentergoodname in goodname:
        PublicImp.log.step_pass(u"购物车移入收藏夹功能验证成功!")
    else:
        PublicImp.log.step_fail(u"购物车移入收藏夹功能验证失败!")

    # 调用公共登录组件退出系统;
    P_Login_out_web.Login_and_out.Logout()
    sleep(3)
