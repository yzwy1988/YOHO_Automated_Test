# -*- coding: utf-8 -*-

from time import sleep
from Page import PageImp
from Public import P_Login_out_web

"""
  测试用例描述：商品详情页面--我要评论;
"""


def testcase_addcomment():

    # 调用登录方法
    P_Login_out_web.Login_and_out.Login()
    # 点击品牌一览链接
    PageImp.Page_Home.Page_Home.Brand_View.Click()
    sleep(3)
    # 品牌列表页面--随机点击一个品牌
    PageImp.Page_BrandList.Page_BrandList.Blist.ClickList()
    sleep(3)
    # 随机点击商品列表中的任意商品,进入商品详情页面
    PageImp.Page_SearchResultList.Page_SearchResultList.SelectGoods.ClickList()
    sleep(3)
    # 点击我要评论按钮
    PageImp.Page_GoodsDetails.Page_GoodsDetails.CommentAdd.Click()
    sleep(3)
    # 判断进入个人中心后,主页面的标题是否正确;
    PageImp.Page_PersonalCenter.Page_PersonalCenter.CommentTitle.VerifyInnerHTMLContains(u"我的评论")

    """
    # 个人中心--我的评论--判断是否有未评论的订单,有的话则随机选择一个进行评论;
    if PageImp.Page_PersonalCenter.Page_PersonalCenter.CommentAdd.IsExist():
        PageImp.Page_PersonalCenter.Page_PersonalCenter.CommentAdd.ClickList_App()
        PageImp.Page_PersonalCenter.Page_PersonalCenter.CommentText.Set(unicode("很不错的商品,会继续关注!"))
        PageImp.Page_PersonalCenter.Page_PersonalCenter.CommentSubmit.Click()
    """

    # 退出登录
    P_Login_out_web.Login_and_out.Logout()
