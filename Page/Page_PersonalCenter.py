# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_PersonalCenter:

    # 个人中心--顶部导航栏--YOHO图标
    class headerYOHO(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, '//*[@class="headerYOHO"]')

