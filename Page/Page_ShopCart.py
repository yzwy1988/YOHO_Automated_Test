# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_ShopCart:

    # 购物车--结算按钮
    class ToSettleAccounts(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="calcButton"]')

