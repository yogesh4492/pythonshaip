import pymysql

mydb=pymysql.connect(user="root",host="localhost",password="NewStrongPassword@123",database="jan1")

mycursor=mydb.cursor()

# mycursor.execute("create database  if not exists jan1")

mycursor.execute("show tables")
query="create table if not exists student(id int primary key auto_increment,name text,subject text,score int)"
# name="yogesh"
# subject="python"
# score=89
# values=(name,subject,score)
mycursor.execute(query)
sql="insert into student(name,subject,score) values('%s','%s',%s)"
values=("Yogesh","python",89)
mycursor.execute(sql%values)
mycursor.execute("select *  from student")
result=mycursor.fetchall()
print(result)



mydb.commit()