# -*- coding: utf-8 -*-

from Page import PageImp
from Automan import PublicImp
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class P_Web_ShopCart:

    @classmethod
    def Web_ShopCart(cls):

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
        sleep(5)

        # 结算页面--收货地址--判断是否有默认地址,如果有则跳过此步;如果没有则进入,先判断有没有地址,有则随机选择一个,没有则添加新地址;
        if PageImp.Page_OrderDetails.Page_OrderDetails.editAddress.IsExist():
            pass
        else:
            if PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.IsExist():
                PageImp.Page_OrderDetails.Page_OrderDetails.SelectAddressByRandom.ClickList_App()
            else:
                PageImp.Page_OrderDetails.Page_OrderDetails.addressee_name.Set(unicode("测试"))
                PageImp.Page_OrderDetails.Page_OrderDetails.province.Select("上海市")
                PageImp.Page_OrderDetails.Page_OrderDetails.city.Select("上海市")
                PageImp.Page_OrderDetails.Page_OrderDetails.area_code.SelectByRandomOrder()
                PageImp.Page_OrderDetails.Page_OrderDetails.address.Set(unicode("经济技术开发区 苏源大道87号 (有货物流中心 订单组)"))
                PageImp.Page_OrderDetails.Page_OrderDetails.mobile.Set("13915992963")
                PageImp.Page_OrderDetails.Page_OrderDetails.email.Set("abc@126.com")
                PageImp.Page_OrderDetails.Page_OrderDetails.zip_code.Set("211100")
            PageImp.Page_OrderDetails.Page_OrderDetails.SaveShippingAddress.Click()
            sleep(2)

        # 结算页面--验证支付方式是否为"在线支付"
        if PageImp.Page_OrderDetails.Page_OrderDetails.PayMode.VerifyContentIsIncluded("在线支付"):
            pass
        else:
            # 结算页面--支付及送货时间--修改按钮
            PageImp.Page_OrderDetails.Page_OrderDetails.editPay.Click()
            # 结算页面--选择在线支付
            PageImp.Page_OrderDetails.Page_OrderDetails.pay_type1.Click()
            PageImp.Page_OrderDetails.Page_OrderDetails.PaymentButton.Click()

        # 结算页面,点击页面底部的 去付款 按钮,进入在线支付页面
        PageImp.Page_OrderDetails.Page_OrderDetails.ToPay.Click()
