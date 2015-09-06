# -*- coding: utf-8 -*-

import datetime
import sys
import xlwt
import env
import common


def generate_result_xls():

    wbk = xlwt.Workbook()

    style_bold  = xlwt.easyxf('font: name Microsoft YaHei, height 250, colour black, bold False;  borders: left 1, right 1, top 1, bottom 1, bottom_colour 0x3A;  pattern: pattern solid, fore_colour gray25;')
    style_red   = xlwt.easyxf('font: name Microsoft YaHei, height 200, colour red,   bold False;  borders: left 1, right 1, top 1, bottom 1, bottom_colour 0x3A')
    style_green = xlwt.easyxf('font: name Microsoft YaHei, height 200, colour green, bold False;  borders: left 1, right 1, top 1, bottom 1, bottom_colour 0x3A')
    style_other = xlwt.easyxf('font: name Microsoft YaHei, height 200, colour black, bold False;  borders: left 1, right 1, top 1, bottom 1, bottom_colour 0x3A')

    for m in env.EXCEL_REPORT_DATA:
        if "Name" in m:
            sheet = wbk.add_sheet(m["Name"])
            
            sheet.write(0, 0, 'Test Case Name', style_bold)
            sheet.write(0, 1, 'IE', style_bold)
            sheet.write(0, 2, 'Firefox', style_bold)
            sheet.write(0, 3, 'Chrome', style_bold)
            sheet.write(0, 4, 'Safari', style_bold)
            sheet.write(0, 5, 'Android', style_bold)
            sheet.write(0, 6, 'IOS', style_bold)
            
            sheet.col(0).width = 256 * 50
            sheet.col(1).width = 256 * 15
            sheet.col(2).width = 256 * 15
            sheet.col(3).width = 256 * 15
            sheet.col(4).width = 256 * 15
            sheet.col(5).width = 256 * 15
            sheet.col(6).width = 256 * 15

            i = 1
            for case in m["TestCases"]:
                sheet.write(i, 0, case["Name"], style_other)
                
                if "IE" in case:
                    if case["IE"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 1, case["IE"], style_green)
                    elif case["IE"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 1, case["IE"], style_red)
                else:
                    sheet.write(i, 1, "NO RUN", style_other)

                if "Firefox" in case:
                    if case["Firefox"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 2, case["Firefox"], style_green)
                    elif case["Firefox"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 2, case["Firefox"], style_red)
                else:
                    sheet.write(i, 2, "NO RUN", style_other)
                
                if "Chrome" in case:
                    if case["Chrome"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 3, case["Chrome"], style_green)
                    elif case["Chrome"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 3, case["Chrome"], style_red)
                else:
                    sheet.write(i, 3, "NO RUN", style_other)

                if "Safari" in case:
                    if case["Safari"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 4, case["Safari"], style_green)
                    elif case["Safari"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 4, case["Safari"], style_red)
                else:
                    sheet.write(i, 4, "NO RUN", style_other)

                if "Android" in case:
                    if case["Android"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 5, case["Android"], style_green)
                    elif case["Android"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 5, case["Android"], style_red)
                else:
                    sheet.write(i, 5, "NO RUN", style_other)

                if "IOS" in case:
                    if case["IOS"] == "Pass":
                        env.CaseSuccess += 1
                        sheet.write(i, 6, case["IOS"], style_green)
                    elif case["IOS"] == "Fail":
                        env.CaseFail += 1
                        sheet.write(i, 6, case["IOS"], style_red)
                else:
                    sheet.write(i, 6, "NO RUN", style_other)

                i += 1

    wbk.save(common.force_delete_file(u"%s\\Result\\result.xls" % env.PROJECT_PATH))


def add_excel_report_data(list_all=[], module_name="TestModule", case_name="TestCase", browser_type="IE", result="Pass"):
    for module in list_all:
        if module_name == module["Name"]:
            
            for case in module["TestCases"]:
                if case_name == case["Name"]:
                    case[browser_type] = result
                    return list_all
            
            module["TestCases"].append({"Name": case_name, browser_type: result})
            return list_all
    
    list_all.append({"Name": module_name, "TestCases": [{"Name": case_name, browser_type: result}]})
    return list_all


def start_test(case_name):
    env.CASE_NAME       = case_name
    env.CASE_START_TIME = datetime.datetime.now().replace(microsecond=0)
    env.CASE_PASS       = True
    
    common.mkdirs("%s\\Result\\screenshots\\" % env.PROJECT_PATH)
    common.mkdirs("%s\\Result\\testcase\\" % env.PROJECT_PATH)
    
    with open(u"%s\\Result\\testcase\\%s__%s.log" % (env.PROJECT_PATH, env.CASE_NAME, common.stamp_date()), "a") as f:
        f.write(u"\n**************  Test Case [%s] [%s]  ***************\n" % (env.CASE_NAME, env.platformName))


def stop_test():
    env.CASE_STOP_TIME = datetime.datetime.now().replace(microsecond=0)

    with open(u"%s\\Result\\summary.log" % env.PROJECT_PATH, "a") as f:
        env.RUNNING_PASS_OR_FAIL = env.CASE_PASS
        if env.CASE_PASS == True:
            add_excel_report_data(env.EXCEL_REPORT_DATA, env.MODULE_NAME, env.CASE_NAME, env.platformName, "Pass")
            f.write(u"%s    [Pass]  =>  [%s] [%s] [%s]\n" % (common.stamp_datetime(),
                                                            env.CASE_STOP_TIME - env.CASE_START_TIME, 
                                                            env.CASE_NAME, 
                                                            env.platformName))
        else:
            add_excel_report_data(env.EXCEL_REPORT_DATA, env.MODULE_NAME, env.CASE_NAME, env.platformName, "Fail")
            f.write(u"%s    [Fail]  =>  [%s] [%s] [%s] (⊙o⊙) \n" % (common.stamp_datetime(),
                                                                 env.CASE_STOP_TIME - env.CASE_START_TIME, 
                                                                 env.CASE_NAME, 
                                                                 env.platformName))
    
    # generate_result_xls()
    env.CASE_PASS = True


def step_section(message):
    with open(u"%s\\Result\\testcase\\%s__%s.log" % (env.PROJECT_PATH, env.CASE_NAME, common.stamp_date()), "a") as f:
        f.write(u"\n%s    Section: %s\n" % (common.stamp_datetime(), message))


def step_normal(message):
    with open(u"%s\\Result\\testcase\\%s__%s.log" % (env.PROJECT_PATH, env.CASE_NAME, common.stamp_date()), "a") as f:
        f.write(u"%s    Step: %s\n" % (common.stamp_datetime(), message))


def step_pass(message):
    with open(u"%s\\Result\\testcase\\%s__%s.log" % (env.PROJECT_PATH, env.CASE_NAME, common.stamp_date()), "a") as f:
        f.write(u"%s    Pass: %s\n" % (common.stamp_datetime(), message))


def step_fail(message):
    screenshot_name = "%s__%s__Fail__%s.png" % (env.CASE_NAME, env.platformName, common.stamp_datetime_coherent())
    
    with open(u"%s\\Result\\testcase\\%s__%s.log" % (env.PROJECT_PATH, env.CASE_NAME, common.stamp_date()), "a") as f:
        f.write(u"------------ Fail [%s] -------------------\n" % common.stamp_datetime())
        f.write(u"%s    Fail: %s, Check ScreenShot [%s]\n" % (common.stamp_datetime(), message, screenshot_name))
        f.write(u"------------ Fail [%s] --------------------------------------------\n" % common.stamp_datetime())
    
    common.mkdirs("%s\\Result\\screenshots\\" % env.PROJECT_PATH)
    env.driver.save_screenshot(u"%s\\Result\\screenshots\\%s" % (env.PROJECT_PATH, screenshot_name))
    
    env.CASE_PASS = False
    
    raise AssertionError(message)


def handle_error():
    if env.CASE_PASS == False:
        return

    if sys.exc_info()[0] != None:
        step_normal(common.exception_error())
        
        screenshot_name = "%s__%s__Error_%s.png" % (env.CASE_NAME, env.platformName, common.stamp_datetime_coherent())
        
        common.mkdirs("\\Result\\screenshots\\")
        env.driver.save_screenshot(u"%s\\Result\\screenshots\\%s" % (env.PROJECT_PATH, screenshot_name))
        
        step_normal("Please check screen short [%s]" % screenshot_name)

        env.CASE_PASS = False
