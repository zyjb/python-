import pymysql

# 数据库url，账户，密码，端口
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='rfid')
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)

sql = 'select Name from rfid_depot where ID=2'
row = cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
connection.close()