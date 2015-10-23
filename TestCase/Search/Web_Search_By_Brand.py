# -*- coding: utf-8 -*-

from Page import PageImp
from time import sleep


def web_search_by_brand():

    if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
        PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()
        sleep(3)

    searchcontent = u"Nike"
    PageImp.Page_Home.Page_Home.SearchText.Set(searchcontent)
    PageImp.Page_Home.Page_Home.SearchButton.Click()
    sleep(3)

    PageImp.Page_SearchResultList.Page_SearchResultList.SearchBrandResult.\
        VerifyInnerHTMLContains(searchcontent + u"品牌店")
