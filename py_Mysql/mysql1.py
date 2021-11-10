# 导入pymysql包
import pymysql

# user_input = int(input("请输入你要查询的id："))
# 连接信息
user_input = ("小郭",20,"男")
info = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"root",
    "database":"mysql1",
    "charset":"utf8"
}
# 与mysql进行连接
conn = pymysql.connect(**info)
# 创建游标 游标是传输数据的小车，数据都在游标上。
cursor = conn.cursor()
# sql语句
# sql1 = "insert into data1(name, age, gender) values (%s,%s,%s)"
sql2 = "select name from data1"
# 执行sql语句
try:
    # cursor.execute(sql1, user_input)
    cursor.execute(sql2)
    # 获取一行数据，返回元组形式
    row1 = cursor.fetchall()
    for name in row1:
        print(name)
    conn.commit()
except Exception as e:
    conn.rollback()
    # 关闭游标
finally:
    cursor.close()
    # 关闭连接
    conn.close()