# -*- coding: utf-8 -*-

from appium import webdriver
import PublicImp
import importlib
import inspect
import types
import os
import sys
import env
import time
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def launch_browser():

    if env.RUNNING_BROWSER.upper() == "FIREFOX":
        # the end of the browser process , the end of the browser driven process
        os.popen("TASKKILL /F /IM firefoxdriver.exe")

        fp = FirefoxProfile()
        fp.native_events_enabled = False

        binary_path = PublicImp.common.get_value_from_conf("FIREFOX_BINARY_PATH")

        if binary_path == "":
            env.driver = selenium.webdriver.Firefox(firefox_profile=fp)
        else:
            fb = FirefoxBinary(firefox_path=binary_path)
            env.driver = selenium.webdriver.Firefox(firefox_profile=fp, firefox_binary=fb)

    elif env.RUNNING_BROWSER.upper() == "CHROME":
        os.popen("TASKKILL /F /IM chromedriver.exe")

        binary_path = PublicImp.common.get_value_from_conf("CHROME_BINARY_PATH")
        chromedriver = PublicImp.common.get_value_from_conf("DRIVER_CHROME")

        if binary_path == "":
            os.environ["webdriver.chrome.driver"] = chromedriver
            env.driver = selenium.webdriver.Chrome(executable_path=chromedriver)
        else:
            opts = Options()
            opts.binary_location = binary_path
            os.environ["webdriver.chrome.driver"] = chromedriver
            env.driver = selenium.webdriver.Chrome(executable_path=chromedriver, chrome_options=opts)

    elif env.RUNNING_BROWSER.upper() == "IE":
        os.popen("TASKKILL /F /IM IEDriverServer.exe")

        dc = DesiredCapabilities.INTERNETEXPLORER.copy()

        dc['acceptSslCerts'] = True
        dc['nativeEvents'] = True

        iedriver = PublicImp.common.get_value_from_conf("DRIVER_IE")
        os.environ["webdriver.ie.driver"] = iedriver
        env.driver = selenium.webdriver.Ie(executable_path=iedriver, capabilities=dc)

    else:
        return False

    env.platformName = env.RUNNING_BROWSER

    env.TEST_URL = PublicImp.common.get_value_from_conf("TESTING_URL")
    env.driver.get(env.TEST_URL)
    env.driver.maximize_window()

    time.sleep(3)
    env.driver.refresh()
    # env.driver.set_window_size(480, 800)
    time.sleep(3)

    return True


def launch_device():

    xls = PublicImp.datadriver.ExcelSheet("TeseCaseDescription.xlsx", "TeseCaseDescription")
    for j in range(1, xls.nrows()):
        tescaseName = xls.cell(j, "TeseCaseName")
        if tescaseName == env.MODULE_NAME:
            appium_server_ip = xls.cell(j, "appium_server_ip")
            appium_server_port = xls.cell(j, "appium_server_port")
            udid = xls.cell(j, "udid")
            platformVersion = xls.cell(j, "AndroidVersion")

    if env.TESTING_BROWSERS == 'APP-Android':
        desired_caps = {}
        platformName = PublicImp.common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
        # platformVersion = PublicImp.common.get_value_from_conf("platformVersion")
        deviceName = PublicImp.common.get_value_from_conf("deviceName")
        appPackage = PublicImp.common.get_value_from_conf("appPackage")
        appActivity = PublicImp.common.get_value_from_conf("appActivity")
        unicodeKeyboard = PublicImp.common.get_value_from_conf("unicodeKeyboard")
        resetKeyboard = PublicImp.common.get_value_from_conf("resetKeyboard")

        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['udid'] = udid
        desired_caps["unicodeKeyboard"] = unicodeKeyboard
        desired_caps["resetKeyboard"] = resetKeyboard

        env.platformName = platformName

    elif env.TESTING_BROWSERS == 'APP-IOS':
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {}
        platformName = PublicImp.common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
        platformVersion = PublicImp.common.get_value_from_conf("platformVersion")
        deviceName = PublicImp.common.get_value_from_conf("deviceName")
        app = PublicImp.common.get_value_from_conf("app")
        udid = PublicImp.common.get_value_from_conf("udid")
        unicodeKeyboard = PublicImp.common.get_value_from_conf("unicodeKeyboard")
        resetKeyboard = PublicImp.common.get_value_from_conf("resetKeyboard")

        desired_caps['platformName'] = "iOS"
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        # desired_caps['app'] = os.path.abspath('/Users/dingzhou/stone/YOHO_3.3.ipa')
        # desired_caps['app'] = app
        desired_caps['app'] = PATH('/Users/dingzhou/stone/appium_sample-master/app/iOSNative/build/Release-iphonesimulator/ToDoList.app')
        # desired_caps['udid'] = udid
        # desired_caps["unicodeKeyboard"] = unicodeKeyboard
        # desired_caps["resetKeyboard"] = resetKeyboard

    elif env.TESTING_BROWSERS == 'H5-Android':
        desired_caps = {}
        platformName = PublicImp.common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
        # platformVersion = PublicImp.common.get_value_from_conf("platformVersion")
        deviceName = PublicImp.common.get_value_from_conf("deviceName")
        browserName = PublicImp.common.get_value_from_conf("browserName")
        DevicesUrl = PublicImp.common.get_value_from_conf("DevicesUrl")

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps["browserName"] = browserName
        desired_caps['udid'] = udid

        env.platformName = platformName

    elif env.TESTING_BROWSERS == 'H5-IOS':
        desired_caps = {}
        platformName = PublicImp.common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")
        platformVersion = PublicImp.common.get_value_from_conf("platformVersion")
        deviceName = PublicImp.common.get_value_from_conf("deviceName")
        browserName = PublicImp.common.get_value_from_conf("browserName")
        DevicesUrl = PublicImp.common.get_value_from_conf("DevicesUrl")

        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps["browserName"] = browserName

        env.platformName = platformName

    env.driver = webdriver.Remote('http://%s:%s/wd/hub' % (appium_server_ip, appium_server_port), desired_caps)

    if env.TESTING_BROWSERS == 'H5-Android' or env.TESTING_BROWSERS == 'H5-IOS':
        env.driver.get("http://m.yohobuy.com")
        env.driver.implicitly_wait(10)

    return True


def testcase_ending():
    time.sleep(3)
    env.driver.quit()
    # os.popen("taskkill /f /im cmd.exe")
    # os.popen("taskkill /f /im node.exe")


def testcase_windingup():
    time.sleep(3)
    env.driver.quit()

    os.popen("TASKKILL /F /IM IEDriverServer.exe")
    os.popen("TASKKILL /F /IM chromedriver.exe")


def run_module(dirname, module_name):
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

    if dirname == "":
        testmodule = importlib.import_module("TestCase.%s" % module_name)
        testcasename = "TestCase->" + module_name + ".py"
    else:
        testmodule = importlib.import_module("TestCase.%s.%s" % (dirname, module_name))
        testcasename = "TestCase->" + dirname + "->" + module_name + ".py"

    env.MODULE_NAME = module_name.split('.')[-1]
    testcases = [testmodule.__dict__.get(a).__name__ for a in dir(testmodule)
           if isinstance(testmodule.__dict__.get(a), types.FunctionType)]

    env.PROJECT_PATH = os.path.dirname(os.path.abspath(inspect.stack()[1][1]))
    sys.path.append(env.PROJECT_PATH)
    env.TESTING_BROWSERS = PublicImp.common.get_value_from_conf("TESTING_BROWSERS_OR_DEVICES")

    for testcase in testcases:

        if "APP-Android" in env.TESTING_BROWSERS or "APP-IOS" in env.TESTING_BROWSERS or "H5-Android" in env.TESTING_BROWSERS or "H5-IOS" in env.TESTING_BROWSERS:
            rerun_number = PublicImp.common.get_value_from_conf("rerun_num")

            k = 0
            while k < int(rerun_number):
                RUNNING_PASS_OR_FAIL = env.RUNNING_PASS_OR_FAIL
                if RUNNING_PASS_OR_FAIL is False:
                    print("=> %s Runs %s Times in ** %s ** " % (testcase, (k+1), env.TESTING_BROWSERS))

                    if launch_device() is False:
                        continue

                    # Run Test Case.
                    try:
                        PublicImp.log.start_test(testcase)
                        # print("=> Now running the test case %s " % testcase)
                        getattr(testmodule, testcase)()
                        print("=> the test case %s run ** Success ** " % testcase)
                    except:
                        PublicImp.log.handle_error()
                        print("=> the test case %s run ** Fail ** " % testcase)
                    finally:
                        PublicImp.log.stop_test()
                    # print("=> Now end the test case %s " % testcase)

                    testcase_ending()

                k += 1

            env.RUNNING_PASS_OR_FAIL = False

        else:
            for browser in env.TESTING_BROWSERS.split('|'):
                env.RUNNING_BROWSER = browser

                rerun_number = PublicImp.common.get_value_from_conf("rerun_num")

                k = 0
                while k < int(rerun_number):
                    RUNNING_PASS_OR_FAIL = env.RUNNING_PASS_OR_FAIL
                    if RUNNING_PASS_OR_FAIL is False:
                        print("=> %s Runs %s Times in ** %s ** " % (testcasename, (k+1), env.RUNNING_BROWSER))

                        # Launch Browser
                        if "before_launch_browser" in testcases:
                            getattr(testmodule, "before_launch_browser")()

                        if launch_browser() is False:
                            continue

                        # Run Test Case.
                        try:
                            PublicImp.log.start_test(testcase)
                            # print("=> Now running the test case %s " % testcase)

                            if "before_each_testcase" in testcases:
                                getattr(testmodule, "before_each_testcase")()

                            getattr(testmodule, testcase)()
                            print("=> the test case %s run ** Success ** " % testcasename)
                        except:
                            PublicImp.log.handle_error()
                            print("=> the test case %s run ** Fail ** " % testcasename)
                        finally:
                            if "after_each_testcase" in testcases:
                                getattr(testmodule, "after_each_testcase")()

                            PublicImp.log.stop_test()

                        # print("=> Now end the test case %s " % testcase)

                        # Clear Environment. Quite Browser, Kill Driver Processes.
                        testcase_windingup()

                    k += 1

                env.RUNNING_PASS_OR_FAIL = False
