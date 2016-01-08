# -*- coding: utf-8 -*-

from Automan import PublicImp
from time import sleep
from Page import PageImp
from Public import P_Login_out_web


"""
  测试用例描述：未登录情况进行收藏品牌,验证品牌收藏是否成功;
"""


def Web_CollectBrand_Without_Login():

    if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
        PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()
        sleep(3)

    # 点击品牌一览链接
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    # 获取所有品牌总数，并且随机点一个品牌
    sleep(5)
    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    sleep(5)
    # 点击收藏按钮
    PageImp.Page_SearchResultList.Page_SearchResultList.BrandFavor.Click_No_Switch()
    sleep(5)

    xls = PublicImp.datadriver.ExcelSheet("LoginUserData_web.xlsx", "gload_login")
    for i in range(1, xls.nrows()):
        PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
        exc_account = xls.cell(i, "UserName")
        exc_password = xls.cell(i, "Password")
        PageImp.Page_Login.Page_Login.UserName.Set(exc_account)
        PageImp.Page_Login.Page_Login.UserName.Click()
        PageImp.Page_Login.Page_Login.PassWord.Set(exc_password)
        sleep(3)
    PageImp.Page_Login.Page_Login.SubmitButton.Click()
    sleep(5)
    PageImp.Page_SearchResultList.Page_SearchResultList.BrandFavor.Click_No_Switch()

    # 点击我的收藏链接，进入我的收藏夹
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()

    js = "var q = document.documentElement.scrollTop=100000"
    PublicImp.env.driver.execute_script(js)

    # 点击品牌收藏链接
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_BrandCollectTab.Click()
    sleep(5)

    # 验证是否存在收藏的品牌
    # ln = PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_GetBrandName.GetObjectsCount()
    # if ln == 0:
    #     PublicImp.log.step_fail(u"收藏品牌失败")

    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_SelectAllBrand.Click_No_Switch()
    sleep(3)
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_RemoveBrand.Click_No_Switch()
    sleep(3)
    PublicImp.webelement.WebBrowser.AlertAccept()
    sleep(3)

    # 退出登录
    PageImp.Page_Home.Page_Home.Logout.Click()
