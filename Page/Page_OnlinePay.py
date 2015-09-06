# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_OnlinePay:

    # 在线支付页面--订单号
    class GetOrderNumber(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="cartnew-pay"]/h3/strong[1]')

    # 在线支付页面--导航栏中的 订单中心 链接
    class GoToOrderCenter(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[contains(@class,"simple-items")]/li[3]//a')

