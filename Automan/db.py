# coding=utf-8

import MySQLdb


def dbconnect():

    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='*****',
            db='test',
            use_unicode=True,
            charset="utf8",
            )
    cur = conn.cursor()

    # 删除数据表
    # cur.execute("drop table executer_result;")

    # 创建数据表
    # cur.execute("create table executer_result(executer_time varchar(50) ,model_name varchar(50) ,testcase_name varchar(50),IE_status varchar(10),Firefox_status varchar(10),Chrome_status varchar(10),Safari_status varchar(10),Android_status varchar(10),IOS_status varchar(10))")

    # 插入一条数据
    # cur.execute("insert into executer_result values('2015-06-19 ','0天0小时4分8秒 ','TTest_Login','testcase01_Login_And_Logout','NO RUN','NO RUN','NO RUN','NO RUN','NO RUN','NO RUN')")

    # 修改查询条件的数据
    # cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    # 删除查询条件的数据
    # cur.execute("delete from student where age='9'")

    cur.close()
    conn.commit()
    conn.close()

dbconnect()
