# -*- coding: utf-8 -*-

import xlrd
import common
import env
import DBUtil
import datadriver
import log
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generatehtml():

    hostfromconf = common.get_value_from_conf("host")
    portfromconf = common.get_value_from_conf("port")
    userfromconf = common.get_value_from_conf("user")
    passwdfromconf = common.get_value_from_conf("passwd")
    dbfromconf = common.get_value_from_conf("db")
    charsetfromconf = common.get_value_from_conf("charset")

    dbconfig = {'host': hostfromconf,
                'port': int(portfromconf),
                'user': userfromconf,
                'passwd': passwdfromconf,
                'db': dbfromconf,
                'charset': charsetfromconf}

    db = DBUtil.MySQL(dbconfig)

    Running_Browser_Devices = common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
    if Running_Browser_Devices.split("|")[0] in ("Chrome", "Firefox", "IE", "Safari"):
        source = "PC-Web"
    elif Running_Browser_Devices == "APP-Android":
        source = "APP-Android"
    elif Running_Browser_Devices == "APP-IOS":
        source = "APP-IOS"
    elif Running_Browser_Devices == "H5-Android":
        source = "H5-Android"
    elif Running_Browser_Devices == "H5-iOS":
        source = "H5-iOS"

    precent = round(float(env.CaseSuccess)/(env.CaseSuccess + env.CaseFail), 4)*100

    template = """
    <html>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <table border="1" style="width: 100%;text-align: center;" cellspacing="0" cellpadding="0">
        <tr>
            <td colspan="11"><font face="微软雅黑" size="4" ><strong>YOHO """ + source + """ Automated Test Report</strong></font></td>
        </tr>
        <tr align="left">
            <td colspan="11"><font color="blue">→Executer_Date： """ + env.ExecuterDate + """</font> <br>
                             <font color="blue">→Executer_Time： """ + env.CalTime + """</font> <br>
                             <font color="blue">→Running_Browser_Devices： """ + Running_Browser_Devices + """</font> <br>
                             <font color="blue">→Executer_Case_Total： """ + str(env.CaseSuccess + env.CaseFail) + """</font> <br>
                             <font color="blue">→Executer_Case_Success： """ + str(env.CaseSuccess) + """</font> <br>
                             <font color="blue">→Executer_Case_Fail： """ + str(env.CaseFail) + """</font> <br>
                             <font color="blue">→Executer_SuccessRate(%)： """ + str(precent) + """% </font>
            </td>
        </tr>
        <tr>
            <td bgColor=#C0C0C0 colspan="3" >Test_Case_Name</td>
            <td bgColor=#C0C0C0 >IE</td>
            <td bgColor=#C0C0C0 >Firefox</td>
            <td bgColor=#C0C0C0 >Chrome</td>
            <td bgColor=#C0C0C0 >Safari</td>
            <td bgColor=#C0C0C0 >APP-Android</td>
            <td bgColor=#C0C0C0 >APP-IOS</td>
            <td bgColor=#C0C0C0 >H5-Android</td>
            <td bgColor=#C0C0C0 >H5-IOS</td>
        </tr>
        <result_trs/>
    </table>
    </html>
    """
    result_trs = ""

    data = xlrd.open_workbook(".\\Result\\result.xls")

    for sheetname in data.sheet_names():
        table = data.sheet_by_name(sheetname)
        nrows = table.nrows
        for i in range(1, nrows):
            excelvalue = table.row_values(i)
            testcasename = excelvalue[0]
            IE_status = excelvalue[1]
            Firefox_status = excelvalue[2]
            Chrome_status = excelvalue[3]
            Safari_status = excelvalue[4]
            Android_status = excelvalue[5]
            IOS_status = excelvalue[6]
            H5_Android_status = excelvalue[7]
            H5_IOS_status = excelvalue[8]

        xls = datadriver.ExcelSheet("TeseCaseDescription.xlsx", "TeseCaseDescription")
        for j in range(1, xls.nrows()):
            log.step_section("Execute TeseCaseDescription Excel Date: Line [%s]" % j)
            tescaseName = xls.cell(j, "TeseCaseName")
            tesecasedescription = xls.cell(j, "TeseCaseDescription")
            if sheetname == tescaseName:
                break

        sql = "insert into executer_result values('" + env.ExecuterDate + "','" + sheetname + "','" + testcasename + "','" + IE_status + "','" + Firefox_status + "','" + Chrome_status + "','" + Safari_status + "','" + Android_status + "','" + IOS_status + "','" + H5_Android_status + "','" + H5_IOS_status + "')"
        db.insert(sql)

        result_tr = "<tr><td style="'text-align:left'" >" + tesecasedescription + "</td><td style="'text-align:left'" >" + sheetname + "</td><td style="'text-align:left'" >" + testcasename + "</td>"

        # IE_status
        if IE_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + IE_status + "</td>"
        elif IE_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + IE_status + "</td>"
        else:
            result_tr += "<td>" + IE_status + "</td>"

        # Firefox_status
        if Firefox_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + Firefox_status + "</font></td>"
        elif Firefox_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + Firefox_status + "</font></td>"
        else:
            result_tr += "<td>" + Firefox_status + "</td>"

        # Chrome_status
        if Chrome_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + Chrome_status + "</font></td>"
        elif Chrome_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + Chrome_status + "</font></td>"
        else:
            result_tr += "<td>" + Chrome_status + "</td>"

        # Safari_status
        if Safari_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + Safari_status + "</font></td>"
        elif Safari_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + Safari_status + "</font></td>"
        else:
            result_tr += "<td>" + Safari_status + "</td>"

        # Android_status
        if Android_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + Android_status + "</font></td>"
        elif Android_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + Android_status + "</font></td>"
        else:
            result_tr += "<td>" + Android_status + "</td>"

        # IOS_status
        if IOS_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + IOS_status + "</font></td>"
        elif IOS_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + IOS_status + "</font></td>"
        else:
            result_tr += "<td>" + IOS_status + "</td>"

        # H5_Android_status
        if H5_Android_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + H5_Android_status + "</font></td>"
        elif H5_Android_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + H5_Android_status + "</font></td>"
        else:
            result_tr += "<td>" + H5_Android_status + "</td>"

        # H5_IOS_status
        if H5_IOS_status == "Pass":
            result_tr += "<td bgColor=#008000 >" + H5_IOS_status + "</font></td>"
        elif H5_IOS_status == "Fail":
            result_tr += "<td bgColor=#FF0000 >" + H5_IOS_status + "</font></td>"
        else:
            result_tr += "<td>" + H5_IOS_status + "</td>"

        result_trs += result_tr

    db.close()

    html = template.replace("<result_trs/>", result_trs)
    open(".\\Result\\result.html", "w").write(html)
