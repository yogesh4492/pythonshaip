import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="NewStrongPassword@123")


mycursor=mydb.cursor()
# mycursor.execute("create database if not exists dec20")
mycursor.execute("SHOW DATABASES")
for i in  mycursor.fetchall():
    print(i[0])
mycursor.execute("drop database if exists dec20")

mydb.commit()