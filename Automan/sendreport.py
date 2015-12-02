# -*- coding: utf-8 -*-

import time
import common
import generatehtml
import env
import sys
import smtplib
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

    Running_Browser_Devices = common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
    if Running_Browser_Devices.split("|")[0] in ("Chrome", "Firefox", "IE", "Safari"):
        source = "PC-Web"
    elif Running_Browser_Devices == "APP-Android":
        source = "APP-Android"
    elif Running_Browser_Devices == "APP-IOS":
        source = "APP-IOS"
    elif Running_Browser_Devices == "H5-Android":
        source = "H5-Android"
    elif Running_Browser_Devices == "H5-IOS":
        source = "H5-IOS"

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

        failnum = env.CaseFail
        if failnum >= 1:
            msgRoot['Subject'] = u"[%s Fail] YOHO %s Automated Test Report ( %s )" % (failnum, source, env.ExecuterDate)
        else:
            msgRoot['Subject'] = u"YOHO %s Automated Test Report ( %s )" % (source, env.ExecuterDate)
        msgRoot['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(smtp_login_name, smtp_login_password)
        smtp.sendmail(mail_from, mail_to, msgRoot.as_string())
        smtp.quit()
    print('=> Email has send out !')


def sendreport():
    generatehtml.generatehtml()
    sendmail(".\\Result\\result.html")
