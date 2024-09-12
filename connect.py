import pymysql

db_connect = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python-data"
)

cursor = db_connect.cursor()

sql = "INSERT INTO data (id, name, lastname) VALUES ('', 'testt', 'testt')"
cursor.execute(sql)


print(cursor.rowcount, "record inserted!!")