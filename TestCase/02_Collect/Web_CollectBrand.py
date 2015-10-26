# -*- coding: utf-8 -*-

from Automan import PublicImp
from time import sleep
from Page import PageImp
from Public import P_Login_out_web


"""
  测试用例描述：收藏品牌
"""


def testcase_CollectBrand():
    # 调用登录方法
    P_Login_out_web.Login_and_out.Login()
    # 点击我的收藏链接，进入我的收藏夹
    PageImp.Page_Home.Page_Home.My_Favorite_link.Click()
    # 点击品牌收藏链接
    # 判断我的收藏夹是否存在已经收藏的品牌，如果存在，就删除全部
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_BrandCollectTab.Click()
    if PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_GetBrandName.IsExist():
        PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_SelectAllBrand.Click_No_Switch()
        sleep(3)
        PageImp.Page_PersonalCenter.Page_PersonalCenter.Favorite_RemoveBrand.Click_No_Switch()
        sleep(3)
        PublicImp.webelement.WebBrowser.AlertAccept()
        sleep(5)
    # 点击品牌一览链接
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    # 获取所有品牌总数，并且随机点一个品牌
    sleep(5)
    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    sleep(5)
    # 点击收藏按钮
    PageImp.Page_SearchResultList.Page_SearchResultList.BrandFavor.Click_No_Switch()
    sleep(5)
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
    P_Login_out_web.Login_and_out.Logout()
