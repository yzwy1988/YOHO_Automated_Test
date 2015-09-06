# -*- coding: utf-8 -*-

driver = ""

# 运行的浏览器或移动设备
platformName = ""

# Driver of web browser, such as: webdriver.Firefox()
BROWSER = ""

# Root path of the testing project.
PROJECT_PATH = ""

# Test Case/Module variables.
CASE_START_TIME = ""
CASE_STOP_TIME = ""
CASE_NAME = ""
CASE_PASS = ""
MODULE_NAME = ""

# 失败重跑设置
RUNNING_PASS_OR_FAIL = False

# URL of the testing page.
TEST_URL = ""

# RUNNING_BROWSER is one of TESTING_BROWSERS
RUNNING_BROWSER = ""
TESTING_BROWSERS = ""

# data of test result, for generate report in excel.
EXCEL_REPORT_DATA = []

# 开始运行时间
ExecuterDate = ""

# 执行时间差
CalTime = ""

# 执行的测试用例总数
# CaseTotal = 0

# 执行的测试用例中 成功用例数
CaseSuccess = 0

# 执行的测试用例中 失败用例数
CaseFail = 0
