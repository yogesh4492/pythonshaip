import pymysql


mysqlcon=pymysql.connect(host="localhost",user="root",password="NewStrongPassword@123")
cursor=mysqlcon.cursor()

cursor.execute("create database if not exists 9sepdb")

mysqlcon.commit()