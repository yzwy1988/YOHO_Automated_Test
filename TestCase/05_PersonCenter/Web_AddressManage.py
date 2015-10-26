# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from time import sleep

"""
  测试用例描述:
    个人中心--收货地址--添加地址、修改地址、删除地址;
"""


def testcase_addressmanage():
    # 调用公共组件登录系统;
    P_Login_out_web.Login_and_out.Login()
    sleep(5)
    # 点击首页-顶部导航栏中 MY有货 链接;
    PageImp.Page_Home.Page_Home.MyYoho.Click()
    # 个人中心-点击左侧菜单 地址管理
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_AddressManage.Click()
    # 个人中心-地址管理-输入收货人姓名
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AddresseeName.Set(unicode("自动化"))
    # 个人中心-地址管理-选择省份
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Province.Select("江苏省")
    # 个人中心-地址管理-选择市
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_City.Select("南京市")
    # 个人中心-地址管理-选择区县
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AreaCode.Select("江宁区")
    # 个人中心-地址管理-填写具体地址
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Address.Set(unicode("江宁经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
    # 个人中心-地址管理-填写邮编
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_ZipCode.Set("211100")
    # 个人中心-地址管理-填写固定电话
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Phone.Set("")
    # 个人中心-地址管理-填写手机号码
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Mobile.Set("13915992963")
    # 个人中心-地址管理-填写电子邮件
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Email.Set("abc@126.com")
    # 个人中心-地址管理-点击提交信息按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_BtnSubmit.Click()
    # 个人中心-点击左侧菜单 地址管理
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_AddressManage.Click()
    # 添加地址完成后--验证地址列表是否包含刚添加的地址数据
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Addrlist.VerifyInnerHTMLContains("收货人：自动化")
    sleep(5)


# def testcase02_addressmanage_editaddress():
    # 调用公共登录组件登录系统;
    # P_Login_out.Login_out.01_Login()
    # sleep(5)
    # 点击首页-顶部导航栏中 MY有货 链接;
    # Page_Home.NavigationBar.MyYoho.Click()
    # 个人中心-点击左侧菜单 地址管理
    # Page_PersonalCenter.Menu.AddressManage.Click()

    # 个人中心-地址管理-点击 修改 按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_EditAddr.ClickList()
    # 个人中心-地址管理-输入收货人姓名
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AddresseeName.Set(unicode("自动化修改"))
    # 个人中心-地址管理-选择省份
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Province.Select("江苏省")
    # 个人中心-地址管理-选择市
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_City.Select("南京市")
    # 个人中心-地址管理-选择区县
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AreaCode.Select("江宁区")
    # 个人中心-地址管理-填写具体地址
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Address.Set(unicode("江宁经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
    # 个人中心-地址管理-填写邮编
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_ZipCode.Set("211100")
    # 个人中心-地址管理-填写固定电话
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Phone.Set("")
    # 个人中心-地址管理-填写手机号码
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Mobile.Set("13915992963")
    # 个人中心-地址管理-填写电子邮件
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Email.Set("abc1@126.com")
    # 个人中心-地址管理-点击提交信息按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_BtnSubmit.Click()
    # 个人中心-点击左侧菜单 地址管理
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_AddressManage.Click()
    # 修改地址完成后--验证地址列表是否包含刚编辑的地址数据
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Addrlist.VerifyInnerHTMLContains("收货人：自动化修改")
    sleep(5)


# def testcase03_addressmanage_deleteaddress():
    # 调用公共登录组件登录系统;
    # P_Login_out.Login_out.01_Login()
    # sleep(5)
    # 点击首页-顶部导航栏中 MY有货 链接;
    # Page_Home.NavigationBar.MyYoho.Click()
    # 个人中心-点击左侧菜单 地址管理
    # Page_PersonalCenter.Menu.AddressManage.Click()

    # 个人中心-地址管理-点击 删除 按钮
    PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_DeleteAddr.ClickList()

    # 调用公共组件退出系统;
    P_Login_out_web.Login_and_out.Logout()
