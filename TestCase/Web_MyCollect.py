# -*- coding: utf-8 -*-

from Automan import PublicImp
from time import sleep
from Page import PageImp
from Public import P_Login_out_web

# TestCase001_MyCollect:点击收藏夹商品名称，进入商品详情页面
def testcase_MyCollect():
    # 调用登录方法
    P_Login_out_web.Login_and_out.Login()
    # 判断我的收藏夹是否存在已经收藏的商品,如果存在,就删除全部
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()
    if PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Get_GoodName.IsExist():
        PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_SelectAllGoods.Click_No_Switch()
        PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Removebut.Click_No_Switch()
        sleep(2)
        PublicImp.webelement.WebBrowser.AlertAccept()
        sleep(5)
    # 点击品牌一览链接
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    # 获取所有品牌总数
    sleep(5)
    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    sleep(5)
    # 随机点击商品列表中的任意商品
    PageImp.Page_SearchResultList.Page_SearchResultList.SelectGoods.ClickList()
    # name = PageImp.Page_GoodsDetails.Page_GoodsDetails.Goods_Name.GetInnerHTML()
    # print name
    sleep(5)
    # 点击收藏，将商品加入到我的收藏夹
    PageImp.Page_GoodsDetails.Page_GoodsDetails.Button_Favor.Click_No_Switch()
    # 点击我的收藏链接，进入我的收藏夹
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()

    # 判断是否存在收藏的商品
    # PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Get_GoodName.VerifyInnerHTMLContains(name)
    # 点击商品名称链接进入商品详情页面
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Get_GoodName.Click()

    # 点击商品详情页面的取消收藏按钮
    PageImp.Page_GoodsDetails.Page_GoodsDetails.Button_Favor.Click_No_Switch()

    # 点击我的收藏链接，进入收藏夹
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()
    # 判断是否存在收藏的商品
    ln = PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Get_GoodName.GetObjectsCount()
    if ln > 0:
        PublicImp.log.step_fail(u"取消收藏商品失败")
    sleep(3)

    # 退出登录
    P_Login_out_web.Login_and_out.Logout()
