# -*- coding: utf-8 -*-

from Page import PageImp
from time import sleep

"""
  测试用例描述：搜索商品名,验证搜索结果商品名称中是否包含搜索的内容;
"""


def web_search_by_good():

    if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
        PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()
        sleep(3)

    searchcontent = u"迷彩"
    PageImp.Page_Home.Page_Home.SearchText.Set(searchcontent)
    PageImp.Page_Home.Page_Home.SearchButton.Click()
    sleep(3)

    i = 0
    while i < 10:
        PageImp.Page_SearchResultList.Page_SearchResultList.GetProductNameList.VerifyInnerHTMLContainsByRandom(searchcontent)
        if PageImp.Page_SearchResultList.Page_SearchResultList.NextPage.IsExist():
            PageImp.Page_SearchResultList.Page_SearchResultList.NextPage.Click()
            sleep(3)
        i += 1
