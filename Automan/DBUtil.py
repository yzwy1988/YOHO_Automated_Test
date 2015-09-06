# -*- coding: utf-8 -*-

import MySQLdb
import time
import common


class MySQL:
    u""" 对MySQLdb常用函数进行封装的类 """

    # MySQL错误号码
    error_code = ''
    # 本类的实例
    _instance = None
    # 数据库conn
    _conn = None
    # 游标
    _cur = None
    # 默认超时30秒
    _TIMEOUT = 30
    _timecount = 0

    def __init__(self, dbconfig):
        u"""构造器：根据数据库连接参数，创建MySQL连接"""
        try:
            self._conn = MySQLdb.connect(host=dbconfig['host'],
                                         port=dbconfig['port'],
                                         user=dbconfig['user'],
                                         passwd=dbconfig['passwd'],
                                         db=dbconfig['db'],
                                         charset=dbconfig['charset'])
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error! ', e.args[0], e.args[1]
            print(error_msg)

            # 如果没有超过预设超时时间，则再次尝试连接，
            if self._timecount < self._TIMEOUT:
                interval = 5
                self._timecount += interval
                time.sleep(interval)
                return self.__init__(dbconfig)
            else:
                raise Exception(error_msg)

        self._cur = self._conn.cursor()
        self._instance = MySQLdb

    def query(self, sql):
        u"""执行 SELECT 语句"""
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print("Database error code:", e.args[0], e.args[1])
            result = False
        return result

    def update(self, sql):
        u"""执行 UPDATE 及 DELETE 语句"""
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print("Database error code:", e.args[0], e.args[1])
            result = False
        return result

    def insert(self, sql):
        u"""执行 INSERT 语句。如主键为自增长int，则返回新生成的ID"""
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            return False

    def fetchAllRows(self):
        u"""返回结果列表"""
        return self._cur.fetchall()

    def fetchOneRow(self):
        u"""返回一行结果，然后游标指向下一行。到达最后一行以后，返回None"""
        return self._cur.fetchone()

    def getRowCount(self):
        u"""获取结果行数"""
        return self._cur.rowcount

    def commit(self):
        u"""数据库commit操作"""
        self._conn.commit()

    def rollback(self):
        u"""数据库回滚操作"""
        self._conn.rollback()

    def __del__(self):
        u"""释放资源（系统GC自动调用）"""
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        u"""关闭数据库连接"""
        self.__del__()


if __name__ == '__main__':

    currentPath = "E:\TestScript\Python\YOHO_Automated_Test"
    hostfromconf = common.get_value_from_conf_path("host", currentPath)
    portfromconf = common.get_value_from_conf_path("port", currentPath)
    userfromconf = common.get_value_from_conf_path("user", currentPath)
    passwdfromconf = common.get_value_from_conf_path("passwd", currentPath)
    dbfromconf = common.get_value_from_conf_path("db", currentPath)
    charsetfromconf = common.get_value_from_conf_path("charset", currentPath)
    # print(hostfromconf, portfromconf, userfromconf, passwdfromconf, dbfromconf, charsetfromconf)

    # 数据库连接参数
    dbconfig = {'host': hostfromconf,
                'port': int(portfromconf),
                'user': userfromconf,
                'passwd': passwdfromconf,
                'db': dbfromconf,
                'charset': charsetfromconf}

    # 连接数据库，创建这个类的实例
    db = MySQL(dbconfig)

    # 操作数据库
    sql = "SELECT * FROM executer_result"
    db.query(sql)

    # 获取结果列表
    result = db.fetchAllRows()

    # 相当于php里面的var_dump
    print(result)

    # 对行进行循环
    for row in result:
        # 使用下标进行取值
        print(row)

        # 对列进行循环
        # for colum in row:
            # print(colum)

    # 关闭数据库
    db.close()
