# -*- coding: utf-8 -*-

import datetime
import os
import sys
import inspect
import env
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType


def stamp_date_nomal():
    return datetime.datetime.now()


def stamp_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def stamp_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def stamp_datetime_coherent():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


def timediff(timestart, timestop):
    u"""
      求时间差,传入timestart和timestop都是用datetime.datetime.now()的返回值;
      python输出普通格式的时间,用str(datetime.datetime.now())[:19]即可,日期是[:10];
    """
    t = (timestop-timestart)
    time_day = t.days
    s_time = t.seconds
    ms_time = t.microseconds / 1000000
    usedtime = int(s_time + ms_time)
    time_hour = usedtime / 60 / 60
    time_minute = (usedtime - time_hour * 3600) / 60
    time_second = usedtime - time_hour * 3600 - time_minute * 60
    time_micsecond = (t.microseconds - t.microseconds / 1000000) / 1000

    # retstr = u"%d天%d小时%d分%d秒%d毫秒"  % (time_day, time_hour, time_minute, time_second, time_micsecond)
    retstr = u"%d小时%d分%d秒" % (time_hour, time_minute, time_second)
    return retstr


def exception_error():
    error_message = ""
    for i in range(len(inspect.trace())):
        error_line = u"""
                       File:      %s - [%s]
                       Function:  %s
                       Statement: %s
                       -------------------------------------------------------------------------------------------""" \
                       % (
                       inspect.trace()[i][1],
                       inspect.trace()[i][2],
                       inspect.trace()[i][3],
                       inspect.trace()[i][4])
        
        error_message = "%s%s" % (error_message, error_line)

    error_message = u"""Error!
                       %s
                       %s
                       ======================================== Error Message ====================================%s
                       ======================================== Error Message ======================================================""" \
                       % (
                       sys.exc_info()[0],
                       sys.exc_info()[1],
                       error_message)

    return error_message


def add_unique_postfix(fn):
    fn = unicode(fn)
    
    if not os.path.exists(fn):
        return fn

    path, name = os.path.split(fn)
    name, ext = os.path.splitext(name)

    make_fn = lambda i: os.path.join(path, '%s__%d%s' % (name, i, ext))

    for i in xrange(2, sys.maxint):
        uni_fn = make_fn(i)
        if not os.path.exists(uni_fn):
            return uni_fn

    return None


def force_delete_file(file_path):
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            return file_path
        except:
            '''
            print "delete fail. Kill Processes."
            os.popen("TASKKILL /F /IM excel.exe")
            time.sleep(2)
            '''
            return add_unique_postfix(file_path)
    else:
        return file_path


def mkdirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_value_from_conf(key):
    conf_file = u"%s\\conf.ini" % env.PROJECT_PATH
    
    if not os.path.exists(conf_file):
        return ""
    
    if not os.path.isfile(conf_file):
        return ""
    
    try:
        with open(conf_file, 'r') as f:
            while True:
                data = f.readline()
                
                if not data:
                    return ""
                
                if len(data.split('=')) < 2:
                    continue
                
                if data.strip()[0] == "#":
                    continue
                
                if data.split('=')[0].strip() == key:
                    return str(data.split('=', 1)[1].strip())
    except IOError:
        return ""


def get_value_from_conf_path(key, path):
    conf_file = u"%s\\conf.ini" % path

    if not os.path.exists(conf_file):
        return ""

    if not os.path.isfile(conf_file):
        return ""

    try:
        with open(conf_file, 'r') as f:
            while True:
                data = f.readline()

                if not data:
                    return ""

                if len(data.split('=')) < 2:
                    continue

                if data.strip()[0] == "#":
                    continue

                if data.split('=')[0].strip() == key:
                    return str(data.split('=', 1)[1].strip())
    except IOError:
        return ""


def set_network_connection(value):
    """
       设置网络连接情况：
       PublicImp.env.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
       PublicImp.env.driver.set_network_connection(ConnectionType.WIFI_ONLY)
    """
    if value == 0:
        webdriver.Remote.set_network_connection(ConnectionType.NO_CONNECTION)
    elif value == 1:
        webdriver.Remote.set_network_connection(ConnectionType.AIRPLANE_MODE)
    elif value == 2:
        webdriver.Remote.set_network_connection(ConnectionType.WIFI_ONLY)
    elif value == 4:
        webdriver.Remote.set_network_connection(ConnectionType.DATA_ONLY)
    elif value == 6:
        webdriver.Remote.set_network_connection(ConnectionType.ALL_NETWORK_ON)


def get_network_connection():
    """ 获取网络连接状态"""
    return webdriver.Remote.network_connection


if __name__ == "__main__":
    get_network_connection()
