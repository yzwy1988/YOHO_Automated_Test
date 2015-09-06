# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_GoodsDetails:

    # 商品详情页--立即购买
    class ToBuyNow(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="toBuyNow"]')

    # 购买商品--选择颜色
    class AddCartChooseColor(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="addCartChooseColor"]/li')

    # 购买商品--选择尺码
    class AddCartSizeList(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="addCartSizeList"]/li')

    # 购买商品--加入购物车
    class addCartButton(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'addCartButton')

