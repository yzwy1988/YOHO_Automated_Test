# -*- coding: utf-8 -*-

import os
import common


def startServer():
    currentpath = os.getcwdu()
    source_name = common.get_value_from_conf_path("TESTING_BROWSERS_OR_DEVICES", currentpath)
    if source_name in ("APP-Android", "APP-IOS", "H5-Android", "H5-IOS"):
        os.popen("taskkill /f /im cmd.exe")
        os.popen("taskkill /f /im node.exe")
        os.system(os.getcwdu() + '\Bat\StartAppiumServer.Bat')


def endServer():
    os.popen("taskkill /f /im cmd.exe")
    os.popen("taskkill /f /im node.exe")


if __name__ == "__main__":
    startServer()
