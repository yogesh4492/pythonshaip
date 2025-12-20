from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview

screen=Tk()
screen.geometry("500x500")


#tkinter variablke 
name_tk=StringVar()
subject_tk=StringVar()
score_tk=IntVar()

def register():
    global name_tk,score_tk,subject_tk
    
    mydb=pymysql.connect(host="localhost",user="root",password="NewStrongPassword@123",database="9sepdb")

    mycursor=mydb.cursor()

    sql ="insert into student (name,subject,score) values ('%s','%s',%s)"
    values=(name_tk.get(),subject_tk.get(),score_tk.get())


    mycursor.execute(sql%values)
    mydb.commit()
    # messagebox.showinfo(title="Message",detail="record inserted successfully")
    sql="select* from student"
    mycursor.execute(sql)
    res=mycursor.fetchall()

    table.delete(*table.get_children())
    for i in res:
        table.insert("",END,values=i)




label=Label(screen,text="Registration formm")
label.pack()


name_label=Label(screen,text="Enter Your Name = ")
name_label.place(x=10,y=60)

name=Entry(screen,textvariable=name_tk)
name.place(x=160,y=60)
subject_label=Label(screen,text="Enter Your subject = ")
subject_label.place(x=10,y=100)
subject=Entry(screen,textvariable=subject_tk)
subject.place(x=160,y=100)
score_label=Label(screen,text="Enter Your score = ")
score_label.place(x=10,y=140)
score=Entry(screen,textvariable=score_tk)
score.place(x=160,y=140)


btn=Button(screen,text="Submit",command=register)
btn.place(x=170,y=170)
#tree view
table=Treeview(screen,columns=('ID',"NAME","SUBJECT","SCORE"),show="headings")

table.heading("ID",text="ID")
table.heading("NAME",text="NAME")
table.heading("SUBJECT",text="SUBJECT")
table.heading("SCORE",text="SCORE")


table.column("ID",width=30)
table.column("NAME",width=100)
table.column("SUBJECT",width=150)
table.column("SCORE",width=125)

table.place(x=10,y=220)


screen.mainloop()