# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_OrderDetails:

    # 结算页面--去付款按钮
    class ToPay(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'btnSubmitOrder')

    # 结算页面--收货地址--选择第1个地址
    class SelectShippingAddress(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@id="addressBox"]//dl[1]//input')

    # 结算页面--收货地址--保存并送到这个地址 按钮
    class SaveShippingAddress(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@id="address_but"]/a')

    # 结算页面--支付方式
    class PayMode(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'spanPayment')

