# -*- coding: utf-8 -*-

from Page import PageImp
from Automan import PublicImp
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class P_Web_GoodsDetails:

    @classmethod
    def Web_GoodsDetails(cls):

        PublicImp.webelement.WebBrowser.Refresh()
        sleep(5)

        # 商品详情页面,选择颜色（未售罄）
        if PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.GetObjectsCount() > 1:
            PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseColor.ClickList()
        sleep(2)

        # 商品详情页面,选择尺码（未售罄）
        PageImp.Page_GoodsDetails.Page_GoodsDetails.ChooseSize.ClickList()
        sleep(2)

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
