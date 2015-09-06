# -*- coding: utf-8 -*-

from Page import PageImp
from Public import P_Login_out_web
from time import sleep
from Automan import PublicImp

"""
  测试用例描述:
    从AddressData.xlsx表格的address页中读取地址数据进行以下操作：
      1、添加地址;
      2、修改地址;
      3、删除地址;
"""


def testcase_addressmanage_fromexcel():
    # 调用公共组件登录系统;
    P_Login_out_web.Login_and_out.Login()
    sleep(5)
    # 点击首页-顶部导航栏中 MY有货 链接;
    PageImp.Page_Home.Page_Home.MyYoho.Click()
    # 个人中心-点击左侧菜单 地址管理
    PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_AddressManage.Click()

    # 从Excel中读取数据
    xls = PublicImp.datadriver.ExcelSheet("AddressData_web.xlsx", "address")

    for i in range(1, xls.nrows()):
        PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
        addressee_name = xls.cell(i, "addressee_name")
        province = xls.cell(i, "province")
        city = xls.cell(i, 'city')
        area_code = xls.cell(i, 'area_code')
        address = xls.cell(i, 'address')
        zip_code = xls.cell(i, 'zip_code')
        phone = xls.cell(i, 'phone')
        mobile = xls.cell(i, 'mobile')
        email = xls.cell(i, 'email')
        # print("province", province)

        # 个人中心-地址管理-输入收货人姓名
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AddresseeName.Set(unicode(addressee_name))

        if province == "" or city == "" or area_code == "":
            # 个人中心-地址管理-随机选择省份
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Province.SelectByRandomOrder()
            # 个人中心-地址管理-根据省份随机选择市
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_City.SelectByRandomOrder()
            # 个人中心-地址管理-根据市随机选择区县
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AreaCode.SelectByRandomOrder()
        else:
            # 个人中心-地址管理-选择省份
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Province.Select(province)
            # 个人中心-地址管理-选择市
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_City.Select(city)
            # 个人中心-地址管理-选择区县
            PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_AreaCode.Select(area_code)

        # 个人中心-地址管理-填写具体地址
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Address.Set(unicode(address))
        # 个人中心-地址管理-填写邮编
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_ZipCode.Set(zip_code)
        # 个人中心-地址管理-填写固定电话
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Phone.Set(phone)
        # 个人中心-地址管理-填写手机号码
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Mobile.Set(mobile)
        # 个人中心-地址管理-填写电子邮件
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Email.Set(email)
        # 个人中心-地址管理-点击提交信息按钮
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_BtnSubmit.Click()
        # 个人中心-点击左侧菜单 地址管理
        PageImp.Page_PersonalCenter.Page_PersonalCenter.Menu_AddressManage.Click()
        # 添加地址完成后--验证地址列表是否包含刚添加的地址数据
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_Addrlist.VerifyInnerHTMLContains("收货人：" + unicode(addressee_name))
        sleep(5)

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

        # 个人中心-地址管理-点击 删除 按钮
        PageImp.Page_PersonalCenter.Page_PersonalCenter.AddressManage_DeleteAddr.ClickList()

    # 调用公共组件退出系统;
    P_Login_out_web.Login_and_out.Logout()

