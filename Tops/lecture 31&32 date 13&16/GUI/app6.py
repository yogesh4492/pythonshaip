from tkinter import *

screen=Tk()

screen.geometry("500x500")


# tkvsriable 
tkEntry=StringVar()
visibleMSG=StringVar()

def fetchvalue():
    global tkEntry,visibleMSG
    visibleMSG.set(tkEntry.get())
    tkEntry.set("")

lable=Label(screen,text="Enter Your Name = ",font=("Arial",16,"bold"))
lable.place(x=50,y=50)

entry=Entry(screen,textvariable=tkEntry)
entry.place(x=250,y=54)

button=Button(screen,text="Submit",command=fetchvalue)
button.place(x=180,y=120)


label1=Label(screen,textvariable=visibleMSG,font=("arial",16,"bold"))
label1.place(x=180,y=150)

screen.mainloop()