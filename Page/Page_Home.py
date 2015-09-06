# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_Home:

    # 导航栏--用户图标
    class UserLogin(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[contains(@class,"headerUserAvatar")]')

    # 首页--新品上架
    class New(PublicImp.webelement.WebElement):
        (by, value) = (By.LINK_TEXT, '新品上架')

    # 新品列表
    class NewList(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="lazy"]')

