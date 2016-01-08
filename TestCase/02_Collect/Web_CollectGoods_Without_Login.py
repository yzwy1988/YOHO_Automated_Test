# -*- coding: utf-8 -*-

from Automan import PublicImp
from time import sleep
from Page import PageImp
from Public import P_Login_out_web

"""
  测试用例描述：未登录情况进行收藏商品,验证商品收藏是否成功;
"""


def Web_CollectGoods_Without_Login():

    if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
        PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()

    # 点击品牌一览链接
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    # 获取所有品牌总数
    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    # 随机点击商品列表中的任意商品
    PageImp.Page_SearchResultList.Page_SearchResultList.SelectGoods.ClickList()
    # name = PageImp.Page_GoodsDetails.Page_GoodsDetails.Goods_Name.GetInnerHTML()

    # 点击收藏，将商品加入到我的收藏夹
    PageImp.Page_GoodsDetails.Page_GoodsDetails.Button_Favor.Click_No_Switch()

    xls = PublicImp.datadriver.ExcelSheet("LoginUserData_web.xlsx", "gload_login")
    for i in range(1, xls.nrows()):
        PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
        exc_account = xls.cell(i, "UserName")
        exc_password = xls.cell(i, "Password")
        PageImp.Page_Login.Page_Login.UserName.Set(exc_account)
        PageImp.Page_Login.Page_Login.UserName.Click()
        PageImp.Page_Login.Page_Login.PassWord.Set(exc_password)
    PageImp.Page_Login.Page_Login.SubmitButton.Click()
    PageImp.Page_GoodsDetails.Page_GoodsDetails.Button_Favor.Click_No_Switch()

    # 点击我的收藏链接，进入我的收藏夹
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()

    # 判断是否存在收藏的商品
    # PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Get_GoodName.VerifyInnerHTMLContains(name)

    # 删除收藏的商品
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_SelectAllGoods.Click_No_Switch()
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_Removebut.Click_No_Switch()
    PublicImp.webelement.WebBrowser.AlertAccept()
    sleep(3)

    # 退出登录
    PageImp.Page_Home.Page_Home.Logout.Click()
