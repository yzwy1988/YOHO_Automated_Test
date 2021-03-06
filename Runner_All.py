# -*- coding: utf-8 -*-

from Automan import PublicImp
import os
import time


# PC/APP/H5
def run_all_case():
    """测试用例运行总入口"""

    currentpath = os.getcwdu()
    source_name = PublicImp.common.get_value_from_conf_path("TESTING_BROWSERS_OR_DEVICES", currentpath)
    if source_name.split("|")[0] in ("Chrome", "Firefox", "IE", "Safari"):
        source = "Web"
    elif source_name == "APP-Android":
        source = "Android"
    elif source_name == "APP-IOS":
        source = "IOS"
    elif source_name == "H5-Android" or source_name == "H5-IOS":
        source = "H5"

    for filename in os.listdir("TestCase"):
        filepath = os.getcwd() + "\\TestCase\\" + filename
        if os.path.isdir(filepath):
            for filename2 in os.listdir(filepath):
                if filename2.split("_")[0] == source and os.path.splitext(filename2)[1] == '.py':
                    name = filename2.split(".")[0]
                    print("=> **********************************")
                    print("=> Soon Will run the test case ** %s->%s->%s.py **" % ("TestCase", filename, name))
                    PublicImp.executer.run_module(filename, name)
                    # time.sleep(70)
        else:
            if filename.split("_")[0] == source and os.path.splitext(filename)[1] == '.py':
                name = filename.split(".")[0]
                print("=> **********************************")
                print("=> Soon Will run the test case ** %s->%s.py **" % ("TestCase", name))
                PublicImp.executer.run_module("", name)
                # time.sleep(70)

    # 生成\\result\\result.xls文件
    PublicImp.log.generate_result_xls()

# 开启AppiumServer
PublicImp.AppiumServer.startServer()

# 创建PageObject文件
print("=> Generating PageObjects py file from mysql ...")
PublicImp.CreatePageFromDB.create_page_from_db()

# 执行开始时间
Executer_Date = PublicImp.common.stamp_date()
StartTime = PublicImp.common.stamp_date_nomal()

# 运行testcase
run_all_case()

# 执行结束时间
EndTime = PublicImp.common.stamp_date_nomal()

# 计算执行时间差
CalTime = PublicImp.common.timediff(StartTime, EndTime)
PublicImp.env.CalTime = CalTime
PublicImp.env.ExecuterDate = Executer_Date

# 发送测试报告邮件
PublicImp.sendreport.sendreport()

# 停止AppiumServer
PublicImp.AppiumServer.endServer()
