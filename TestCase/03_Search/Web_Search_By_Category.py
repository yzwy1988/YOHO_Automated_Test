# -*- coding: utf-8 -*-

from Automan import PublicImp
from Page import PageImp
from time import sleep

"""
  测试用例描述：搜索品类,验证搜索结果URL地址是否正确;
"""


def web_search_by_category():

    if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
        PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()
        sleep(3)

    searchcontent = u"上衣"
    PageImp.Page_Home.Page_Home.SearchText.Set(unicode(searchcontent))
    PageImp.Page_Home.Page_Home.SearchButton.Click()
    sleep(3)

    # 获取当前的URL
    currenturl = PublicImp.env.driver.current_url

    if currenturl == "http://list.yohobuy.com/?msort=1":
        PublicImp.log.step_pass(u"搜索品类[%s]-验证成功!" % searchcontent)
    else:
        PublicImp.log.step_fail(u"搜索品类[%s]-验证失败!" % searchcontent)
