import pymysql


mydb=pymysql.connect(host="localhost",user="root",password="NewStrongPassword@123")

myCursor=mydb.cursor()


myCursor.execute("create database if not exists 9sepdb")

mydb.commit()
print("datbase created successfully")

mydb=pymysql.connect(host="localhost",user="root",password="NewStrongPassword@123",database="9sepdb")

myCursor=mydb.cursor()


myCursor.execute("create table if not exists student(id int primary key auto_increment,name text,subject text ,score int)")

mydb.commit()
print("table create d successfully")



menu="""
            press 1 for insert record 
            press 2 for view record
            press 3 for delete record


"""
print(menu)

choice=int(input("Enter Your Chopice = "))

if choice==1:
    name=input("Enter Your name")
    subject=input("Enter Subject name= ")
    score=int(input("Enter Yopur Score= "))

    sql="insert into student(name,subject,score) values ('%s','%s',%s)"
    values=(name,subject,score)

    myCursor.execute(sql%values)
    mydb.commit()
    print("REcord Inserted successfully")
elif choice==2:
    sql="select * from student"

    myCursor.execute(sql)
    result=myCursor.fetchall()
    print(result)

elif choice==3:
    id=int(input("Enter Which You want to remove: "))
    sql="delete from student where id = %s"
    args=(id)

    myCursor.execute(sql%args)

    mydb.commit()
    sql="select * from student"

    myCursor.execute(sql)
    result=myCursor.fetchall()
    print(result)