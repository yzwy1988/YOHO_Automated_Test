# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Page import PageImp
from Automan import PublicImp
from time import sleep


class Login_and_out:

    @classmethod
    def Login(cls, account=None, password=None):

        if PageImp.Page_HomeGuide.Page_HomeGuide.Close.IsExist():
            PageImp.Page_HomeGuide.Page_HomeGuide.Close.Click()
            sleep(3)

        PageImp.Page_Home.Page_Home.Login.Click()
        sleep(3)
        if account is not None and password is not None:
            PageImp.Page_Login.Page_Login.UserName.Set(account)
            PageImp.Page_Login.Page_Login.PassWord.Set(password)
        else:
            xls = PublicImp.datadriver.ExcelSheet("LoginUserData_web.xlsx", "gload_login")
            for i in range(1, xls.nrows()):
                PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
                exc_account = xls.cell(i, "UserName")
                exc_password = xls.cell(i, "Password")
                PageImp.Page_Login.Page_Login.UserName.Set(exc_account)
                PageImp.Page_Login.Page_Login.UserName.Click()
                PageImp.Page_Login.Page_Login.PassWord.Set(exc_password)
                sleep(3)
        PageImp.Page_Login.Page_Login.SubmitButton.Click()
        sleep(3)

    @classmethod
    def Logout(cls):
        PageImp.Page_Home.Page_Home.Logout.Click()
