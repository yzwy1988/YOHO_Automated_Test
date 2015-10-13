# -*- coding: utf-8 -*-

from Automan import PublicImp
import os


# Web/APP/H5
def run_all_case():
    """测试用例运行总入口"""

    for filename in os.listdir("TestCase"):
        if filename.split("_")[0] == "Web" and os.path.splitext(filename)[1] == '.py':
            name = filename.split(".")[0]
            print("=> **********************************")
            print("=> Soon Will run the test case ** %s.py **" % name)
            PublicImp.executer.run_module(name)

    # 生成\\result\\result.xls文件
    PublicImp.log.generate_result_xls()

# 执行开始时间
Executer_Date = PublicImp.common.stamp_date()
StartTime = PublicImp.common.stamp_date_nomal()

# 创建PageObject文件
print("=> Generating PageObjects py file from mysql ...")
PublicImp.CreatePageFromDB.create_page_from_db()

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
