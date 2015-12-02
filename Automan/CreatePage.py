# -*- coding: utf-8 -*-

import xlrd
import os
import time
import common


def Create_Page():

    # 获取当前工作目录
    currentPath = os.getcwdu()

    Testing_Browsers_or_Devices = common.get_value_from_conf_path("TESTING_BROWSERS_OR_DEVICES", currentPath)

    if Testing_Browsers_or_Devices == "APP-Android" or Testing_Browsers_or_Devices == "APP-IOS":
        data = xlrd.open_workbook(u"%s\\Data\\PageObjectsData_app.xlsx" % currentPath)
    elif Testing_Browsers_or_Devices == "H5-Android" or Testing_Browsers_or_Devices == "H5-IOS":
        data = xlrd.open_workbook(u"%s\\Data\\PageObjectsData_h5.xlsx" % currentPath)
    else:
        data = xlrd.open_workbook(u"%s\\Data\\PageObjectsData_web.xlsx" % currentPath)

    # 清空Page文件夹
    targetDir = u"%s\\Page" % currentPath
    removeFileInFirstDir(targetDir)

    # 清空result文件夹
    targetDir = u"%s\\Result" % currentPath
    removeFileInFirstDir(targetDir)

    with open(u"%s\\Page\\__init__.py" % currentPath, "a") as f:
            f.write("__author__ = 'lulei'\n\n")

    for sheetname in data.sheet_names():
        table = data.sheet_by_name(sheetname)
        nrows = table.nrows

        with open(u"%s\\Page\\PageImp.py" % currentPath, "a") as f:
            f.write("\nfrom Page import %s" % sheetname)

        with open(u"%s\\Page\\%s.py" % (currentPath, sheetname), "a") as f:
            f.write("# -*- coding: utf-8 -*-\n\n")
            f.write("from Automan import PublicImp\n")
            f.write("from selenium.webdriver.common.by import By\n\n\n")
            f.write("class %s:\n\n" % sheetname)
            for i in range(1, nrows):
                excelvalue = table.row_values(i)
                Element = excelvalue[0]
                ByWay = excelvalue[1]
                VALUE = excelvalue[2]
                Description = excelvalue[3]
                f.write("    # %s\n" % Description)
                f.write("    class %s(PublicImp.webelement.WebElement):\n" % Element)
                f.write("        (by, value) = (By.%s, '%s')\n\n" % (ByWay, VALUE))

    time.sleep(10)


def removeFileInFirstDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)


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
