# -*- coding: utf-8 -*-

from Page import PageImp
from Automan import PublicImp
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


class Login_And_out():

    @classmethod
    def Login(cls, account=None, password=None):

        if PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.IsExist():
            PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.Click()
        sleep(3)

        if PageImp.Page_Home.Page_Home.ad_close.IsExist():
            PageImp.Page_Home.Page_Home.ad_close.Click()

        sleep(5)
        if PageImp.Page_Home.Page_Home.update_cancel.IsExist():
            PageImp.Page_Home.Page_Home.update_cancel.Click()

        PageImp.Page_Home.Page_Home.tabMain_my.Click()
        sleep(2)

        if PageImp.Page_PersonCenter.Page_PersonCenter.loginAndRegisterBtn.IsExist():
            PageImp.Page_PersonCenter.Page_PersonCenter.loginAndRegisterBtn.Click()
            sleep(2)
        else:
            Login_And_out.Logout()
            sleep(2)
            PageImp.Page_PersonCenter.Page_PersonCenter.loginAndRegisterBtn.Click()
            sleep(2)

        if PageImp.Page_Login_Register.Page_Login_Register.Login_del_image.IsExist():
            PageImp.Page_Login_Register.Page_Login_Register.Login_del_image.Click()
            sleep(2)

        if account is not None and password is not None:
            PageImp.Page_Login_Register.Page_Login_Register.Login_username.Set(account)
            sleep(2)
            PageImp.Page_Login_Register.Page_Login_Register.Login_password.Set(password)
        else:
            xls = PublicImp.datadriver.ExcelSheet("LoginUserData_app.xlsx", "LoginAccount")
            for i in range(1, xls.nrows()):
                PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
                exc_account = xls.cell(i, "UserName")
                exc_password = xls.cell(i, "Password")
                PageImp.Page_Login_Register.Page_Login_Register.Login_username.Set(exc_account)
                sleep(2)
                PageImp.Page_Login_Register.Page_Login_Register.Login_password.Set(exc_password)
                sleep(2)
        PageImp.Page_Login_Register.Page_Login_Register.Login_loginbtn.Click()
        sleep(2)

        i = 0
        while i <= 5:
            if PageImp.Page_Login_Register.Page_Login_Register.Login_loginbtn.IsExist():
                PageImp.Page_Login_Register.Page_Login_Register.Login_loginbtn.Click()
            i += 1
        sleep(10)

    @classmethod
    def Logout(cls):
        PageImp.Page_PersonCenter.Page_PersonCenter.settingBtn.Click()
        sleep(2)
        PageImp.Page_PersonCenter.Page_PersonCenter.logoutBtn.Click()
        sleep(2)
