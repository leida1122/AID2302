"""
pymysql 操作数据库
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='debian-sys-maint',
                     password='LpaMozjMR8lOxgQ7',
                     database='stu',
                     charset='utf8')

# 获取游标，执行sql语句
cur = db.cursor()

# 执行sql语句
sql = "insert into class_1 values(7,'bob',15,'w',89.5,'2019-8-8');"
cur.execute(sql)

# 提交写语句
db.commit()

# 关闭数据库连接
cur.close()
db.close()