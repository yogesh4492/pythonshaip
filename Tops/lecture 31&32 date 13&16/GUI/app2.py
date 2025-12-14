"""
.pack() :  it will setup as top , right , left, bottom

.grid(row=0,column=0) : it will setup as grid wise


.place(x=0,y=0) : x axis and y axis
"""

from tkinter import *

screen =Tk()
screen.geometry("500x500")
screen.config(background="#37474f")

lbl=Label(screen,text="Welcom eto myapp",font=("arial",26,"bold"),bg="#37474f",fg="white")
lbl.pack()

screen.mainloop()
