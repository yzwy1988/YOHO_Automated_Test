# -*- coding: utf-8 -*-

from Page import PageImp
from Automan import PublicImp
from time import sleep


class Login_And_out():

    @classmethod
    def login(cls, account=None, password=None):
        sleep(10)
        PageImp.Page_HomeGuide.Page_HomeGuide.GoBoys.Click()
        sleep(10)
        PageImp.Page_Home.Page_Home.UserLogin.Click()
        sleep(2)

        # if PageImp.Page_Login.Page_Login.Login_del_image.IsExist():
            # PageImp.Page_Login.Page_Login.Login_del_image.Click()
            # sleep(2)

        if account is not None and password is not None:
            PageImp.Page_Login.Page_Login.UserName.Set(account)
            sleep(2)
            PageImp.Page_Login.Page_Login.PassWord.Set(password)
        else:
            xls = PublicImp.datadriver.ExcelSheet("LoginUserData_h5.xlsx", "LoginAccount")
            for i in range(1, xls.nrows()):
                PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
                exc_account = xls.cell(i, "UserName")
                exc_password = xls.cell(i, "Password")
                PageImp.Page_Login.Page_Login.UserName.Set(exc_account)
                sleep(2)
                PageImp.Page_Login.Page_Login.PassWord.Set(exc_password)
                sleep(2)
        PageImp.Page_Login.Page_Login.Login_loginbtn.Click_No_Switch()
        sleep(20)

    @classmethod
    def logout(cls):
        PageImp.Page_Login.Page_Login.Logout.Click()
        sleep(2)
