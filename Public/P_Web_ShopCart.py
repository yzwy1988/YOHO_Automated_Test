# -*- coding: utf-8 -*-

from Page import PageImp
from Automan import PublicImp
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class P_Web_ShopCart:

    @classmethod
    def Web_ShopCartList(cls):

        # 购物车页面-选择赠品
        if PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng.IsExist():
            PageImp.Page_ShopCart.Page_ShopCart.Select_Mark_Zeng.Click()
            PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Color.ClickList()
            PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_Select_Size.ClickList()
            PageImp.Page_ShopCart.Page_ShopCart.Mark_Zeng_AddToCart.Click()
            sleep(5)

        # 购物车-选择加价购
        i = 0
        while i < 5:
            if PageImp.Page_ShopCart.Page_ShopCart.SelectNeedPay.IsExist():
                PageImp.Page_ShopCart.Page_ShopCart.SelectNeedPay.ClickList_App()
                if PageImp.Page_ShopCart.Page_ShopCart.btn_sellout.IsExist():
                    PageImp.Page_ShopCart.Page_ShopCart.Close.Click()
                else:
                    PageImp.Page_ShopCart.Page_ShopCart.SelectColor.ClickList()
                    PageImp.Page_ShopCart.Page_ShopCart.SelectSize.ClickList()
                    PageImp.Page_ShopCart.Page_ShopCart.AddToCart.Click()
                    break
                i += 1
            else:
                break

        # 购物车列表页面点击去结算按钮
        PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()

        if PageImp.Page_Login.Page_Login.UserName.IsExist():
            xls = PublicImp.datadriver.ExcelSheet("LoginUserData_web.xlsx", "gload_login")
            for i in range(1, xls.nrows()):
                PublicImp.log.step_section("Execute Excel Date: Line [%s]" % i)
                exc_account = xls.cell(i, "UserName")
                exc_password = xls.cell(i, "Password")
                PageImp.Page_Login.Page_Login.UserName.Set(exc_account)
                PageImp.Page_Login.Page_Login.UserName.Click()
                PageImp.Page_Login.Page_Login.PassWord.Set(exc_password)
            PageImp.Page_Login.Page_Login.SubmitButton.Click()
            sleep(3)

            PageImp.Page_ShopCart.Page_ShopCart.ToSettleAccounts.Click()

    @classmethod
    def Web_ConfirmOrder(cls, pay_type, express):
        # 结算页面--收货地址--判断是否有默认地址,如果有则跳过此步;如果没有则进入,先判断有没有地址,有则随机选择一个,没有则添加新地址;
        if PageImp.Page_OrderDetails.Page_OrderDetails.editAddress.IsExist():
            pass
        else:
            if PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.IsExist():
                PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.ClickList_App()
            else:
                PageImp.Page_OrderDetails.Page_OrderDetails.addressee_name.Set(unicode("测试"))
                PageImp.Page_OrderDetails.Page_OrderDetails.province.SelectByRandomOrder()
                PageImp.Page_OrderDetails.Page_OrderDetails.city.SelectByRandomOrder()
                PageImp.Page_OrderDetails.Page_OrderDetails.area_code.SelectByRandomOrder()
                PageImp.Page_OrderDetails.Page_OrderDetails.address.Set(unicode("经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
                PageImp.Page_OrderDetails.Page_OrderDetails.mobile.Set("13915992963")
                PageImp.Page_OrderDetails.Page_OrderDetails.email.Set("abc@126.com")
                PageImp.Page_OrderDetails.Page_OrderDetails.zip_code.Set("211100")
            PageImp.Page_OrderDetails.Page_OrderDetails.SaveShippingAddress.Click()
            sleep(2)

        # 结算页面--支付及送货时间--修改按钮
        if PageImp.Page_OrderDetails.Page_OrderDetails.editPay.IsExist():
            PageImp.Page_OrderDetails.Page_OrderDetails.editPay.Click()

        # 结算页面--选择支付方式（1在线支付 2货到付款）
        if pay_type == 1:
            PageImp.Page_OrderDetails.Page_OrderDetails.pay_type1.Click()
        elif pay_type == 2:
            if PageImp.Page_OrderDetails.Page_OrderDetails.pay_type2.IsExist():
                PageImp.Page_OrderDetails.Page_OrderDetails.pay_type2.Click()
            else:
                PageImp.Page_OrderDetails.Page_OrderDetails.pay_type1.Click()

        # 结算页面--选择支付及送货时间
        PageImp.Page_OrderDetails.Page_OrderDetails.SelectDeliverTime.ClickList_App()
        PageImp.Page_OrderDetails.Page_OrderDetails.ContactBeforeDelivery.ClickList_App()

        # 结算页面--支付及送货时间--确定按钮
        PageImp.Page_OrderDetails.Page_OrderDetails.PaymentButton.Click()

        # 结算页面--选择快递（1普通快递 2顺丰速运）
        if express == 1:
            PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_Ordinary.Click()
        elif express == 2:
            if PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_shunfeng.IsExist():
                PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_shunfeng.Click()
            else:
                PageImp.Page_OrderDetails.Page_OrderDetails.ShippingManner_Ordinary.Click()

        # 结算页面--索要发票、添加备注信息
        PageImp.Page_OrderDetails.Page_OrderDetails.ShowInvoices.Click()
        PageImp.Page_OrderDetails.Page_OrderDetails.InvoicesPayable.Set(unicode("YOHO"))
        PageImp.Page_OrderDetails.Page_OrderDetails.invoicesType.SelectByRandomOrder()

        PageImp.Page_OrderDetails.Page_OrderDetails.ShowRemark.Click()
        PageImp.Page_OrderDetails.Page_OrderDetails.Remark.Set(unicode("YOHO备注信息"))
        PageImp.Page_OrderDetails.Page_OrderDetails.RemarkBox.ClickList_App()

        # 结算页面,点击页面底部的 去付款 按钮,进入在线支付页面
        PageImp.Page_OrderDetails.Page_OrderDetails.ToPay.Click()
