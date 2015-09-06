# -*- coding: utf-8 -*-

import time
import xlrd
import common
import env
import DBUtil
import sys
import smtplib
import MySQLdb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding('utf8')


def sendmail(file_new):
    mail_from = common.get_value_from_conf("mail_from")
    mailto = common.get_value_from_conf("mail_to")

    smtp_server = common.get_value_from_conf("smtp_server")
    smtp_login_name = common.get_value_from_conf("smtp_login_name")
    smtp_login_password = common.get_value_from_conf("smtp_login_password")

    for mail_to in mailto.split('|'):
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()

        msgRoot = MIMEMultipart('related')

        msgText = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msgRoot.attach(msgText)

        # 构造附件
        att1 = MIMEText(open('.\\Result\\result.html', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="YOHO_autotest_result.html"'
        msgRoot.attach(att1)

        att2 = MIMEText(open('.\\Result\\summary.log', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="YOHO_autotest_summary.log"'
        msgRoot.attach(att2)

        att3 = MIMEText(open('.\\Result\\result.xls', 'rb').read(), 'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="YOHO_autotest_result.xls"'
        msgRoot.attach(att3)

        msgRoot['Subject'] = u"YOHO Automated Test Report ( %s )" % env.ExecuterDate
        msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(smtp_login_name, smtp_login_password)
        smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
        smtp.quit()
    print('=> Email has send out !')


def sendreport():
    generatehtml()
    sendmail(".\\Result\\result.html")


def generatehtml():

    hostfromconf = common.get_value_from_conf("host")
    portfromconf = common.get_value_from_conf("port")
    userfromconf = common.get_value_from_conf("user")
    passwdfromconf = common.get_value_from_conf("passwd")
    dbfromconf = common.get_value_from_conf("db")
    charsetfromconf = common.get_value_from_conf("charset")
    # print(hostfromconf, portfromconf, userfromconf, passwdfromconf, dbfromconf, charsetfromconf)

    """
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='*****',
        db='test',
        use_unicode=True,
        charset="utf8",
        )
    """

    dbconfig = {'host': hostfromconf,
                'port': int(portfromconf),
                'user': userfromconf,
                'passwd': passwdfromconf,
                'db': dbfromconf,
                'charset': charsetfromconf}

    db = DBUtil.MySQL(dbconfig)

    # cur = conn.cursor()

    Running_Browser_Devices = common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")

    template = """
    <html>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <table border="1" style="width: 100%;text-align: center;" cellspacing="0" cellpadding="0">
        <tr>
            <td colspan="8"><font face="微软雅黑" size="4" ><strong>YOHO Automated Test Report</strong></font></td>
        </tr>
        <tr align="left">
            <td colspan="8"><font color="blue">Executer_Date：""" + env.ExecuterDate + """</font> <br>
                            <font color="blue">Executer_Time：""" + env.CalTime + """</font> <br>
                            <font color="blue">Running_Browser_Devices：""" + Running_Browser_Devices + """</font> <br>
                            <font color="blue">Executer_Case_Total：""" + str(env.CaseSuccess + env.CaseFail) + """</font> <br>
                            <font color="blue">Executer_Case_Success：""" + str(env.CaseSuccess) + """</font> <br>
                            <font color="blue">Executer_Case_Fail：""" + str(env.CaseFail) + """</font>
            </td>
        </tr>
        <tr>
            <td bgColor=#C0C0C0 colspan="2" >Test_Case_Name</td>
            <td bgColor=#C0C0C0 >IE</td>
            <td bgColor=#C0C0C0 >Firefox</td>
            <td bgColor=#C0C0C0 >Chrome</td>
            <td bgColor=#C0C0C0 >Safari</td>
            <td bgColor=#C0C0C0 >Android</td>
            <td bgColor=#C0C0C0 >IOS</td>
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

        # cur.execute("insert into executer_result values('" + env.ExecuterDate + "','" + sheetname + "','" + testcasename + "','" + IE_status + "','" + Firefox_status + "','" + Chrome_status + "','" + Safari_status + "','" + Android_status + "','" + IOS_status + "')")
        # conn.commit()
        sql = "insert into executer_result values('" + env.ExecuterDate + "','" + sheetname + "','" + testcasename + "','" + IE_status + "','" + Firefox_status + "','" + Chrome_status + "','" + Safari_status + "','" + Android_status + "','" + IOS_status + "')"
        db.insert(sql)

        result_tr = "<tr><td style="'text-align:left'" >" + sheetname + "</td><td style="'text-align:left'" >" + testcasename + "</td>"

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

        result_trs += result_tr

    # cur.close()
    # conn.close()
    db.close()

    html = template.replace("<result_trs/>", result_trs)

    open(".\\Result\\result.html", "w").write(html)
