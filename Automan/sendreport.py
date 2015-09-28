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
    generatehtml.generatehtml()
    sendmail(".\\Result\\result.html")
