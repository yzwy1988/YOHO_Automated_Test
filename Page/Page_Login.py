# -*- coding: utf-8 -*-

from Automan import PublicImp
from selenium.webdriver.common.by import By


class Page_Login:

    # 登录页面-用户名
    class UserName(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'account')

    # 登录页面-密码
    class PassWord(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'pwd')

    # 登录页面-用户名右侧的X图标
    class Login_del_image(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'x')

    # 登录页面-登录按钮
    class Login_loginbtn(PublicImp.webelement.WebElement):
        (by, value) = (By.ID, 'btn-login')

    # 退出
    class Logout(PublicImp.webelement.WebElement):
        (by, value) = (By.XPATH, '//*[@class="newloginType"]//a[3]')

