# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_HomeGuide:

    # 女生 GIRLS
    class GoGirls(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[contains(@class,"middle-pan")]/a[2]')

    # 男生 BOYS
    class GoBoys(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[contains(@class,"middle-pan")]/a[1]')

