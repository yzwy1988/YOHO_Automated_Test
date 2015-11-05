# -*- coding: utf-8 -*-

import os
import time
import common
import DBUtil
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def create_page_from_db():

    # 获取当前工作目录
    currentPath = os.getcwdu()

    project_name = common.get_value_from_conf_path("PROJECT_NAME", currentPath)
    source_name = common.get_value_from_conf_path("TESTING_BROWSERS_OR_DEVICES", currentPath)

    if project_name == "YOHO":
        project_id = 11
    elif project_name == "SHOW":
        project_id = 12
    elif project_name == "ZIXUN":
        project_id = 13

    if source_name.split("|")[0] in ("Chrome", "Firefox", "IE", "Safari"):
        source_id = 21
    elif source_name == "APP-Android":
        source_id = 22
    elif source_name == "APP-IOS":
        source_id = 23
    elif source_name == "H5-Android" or source_name == "H5-iOS":
        source_id = 24

    # 清空Page文件夹
    targetDir = u"%s\\Page" % currentPath
    removefileinfirstfir(targetDir)

    # 清空result文件夹
    targetDir = u"%s\\Result" % currentPath
    removefileinfirstfir(targetDir)

    hostfromconf = common.get_value_from_conf_path("host", currentPath)
    portfromconf = int(common.get_value_from_conf_path("port", currentPath))
    userfromconf = common.get_value_from_conf_path("user", currentPath)
    passwdfromconf = common.get_value_from_conf_path("passwd", currentPath)
    dbfromconf = common.get_value_from_conf_path("db", currentPath)
    charsetfromconf = common.get_value_from_conf_path("charset", currentPath)
    print(portfromconf, hostfromconf, type(portfromconf))

    dbconfig = {'host': hostfromconf,
                'port': (int)(portfromconf),
                'user': userfromconf,
                'passwd': passwdfromconf,
                'db': dbfromconf,
                'charset': charsetfromconf}

    db = DBUtil.MySQL(dbconfig)

    with open(u"%s\\Page\\__init__.py" % currentPath, "a") as f:
            f.write("__author__ = 'YOHO'\n\n")

    sql = "SELECT DISTINCT a.page_id ,b.pagename_cn FROM yoho_pageobject a, yoho_pagename b, " \
          "yoho_project c, yoho_source d WHERE a.page_id = b.id AND a.project_id=c.id AND a.source_id=d.id " \
          "AND a.state='A' and a.project_id=" + str(project_id) + \
          " and a.source_id=" + str(source_id) + " order by a.id asc "

    db.query(sql)
    result = db.fetchAllRows()
    for row in result:
        page_id = row[0]
        sheetname = row[1]
        with open(u"%s\\Page\\PageImp.py" % currentPath, "a") as f:
            f.write("\nfrom Page import %s" % sheetname)

        with open(u"%s\\Page\\%s.py" % (currentPath, sheetname), "a") as f:
            f.write("# -*- coding: utf-8 -*-\n\n")
            f.write("from Automan import PublicImp\n")
            f.write("from selenium.webdriver.common.by import By\n\n\n")
            f.write("class %s:\n\n" % sheetname)

            sql2 = "SELECT a.id, b.name project_name, c.name source_name, a.page_id, d.pagename_zn ," \
                   "d.pagename_cn, a.pageelement, e.name by_name, a.elementvalue, a.description " \
                   "FROM yoho_pageobject a, yoho_project b, yoho_source c, yoho_pagename d, yoho_by e " \
                   "WHERE a.project_id = b.id AND a.source_id = c.id AND a.page_id = d.id AND a.by_id = e.id" \
                   " AND a.state = 'A' and a.page_id = " + str(page_id)

            db.query(sql2)
            result2 = db.fetchAllRows()
            for row2 in result2:
                element = row2[6]
                byway = row2[7]
                value = row2[8]
                description = row2[9]
                f.write("    # %s\n" % description)
                f.write("    class %s(PublicImp.webelement.WebElement):\n" % element)
                f.write("        (by, value) = (By.%s, '%s')\n\n" % (byway, value))

        time.sleep(2)

    print("=> create_page_from_db finish ! ")
    db.close()


def removefileinfirstfir(targetdir):
    for filename in os.listdir(targetdir):
        targetfile = os.path.join(targetdir, filename)
        if os.path.isfile(targetfile):
            os.remove(targetfile)


def delete_file_folder(src):
    """delete files and folders"""
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


if __name__ == '__main__':
    create_page_from_db()


