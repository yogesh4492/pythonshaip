from tkinter import *

screen=Tk()
screen.geometry("500x500")
screen.config(background="#37474f")

btn=Button(screen,text="ONE",bg="black",fg="white",height=3,width=5)
btn.grid(row=0,column=0)

btn=Button(screen,text="Two",bg="black",fg="white",height=3,width=5)
btn.grid(row=0,column=1)

btn=Button(screen,text="Three",bg="black",fg="white",height=3,width=5)
btn.grid(row=1,column=0)

btn=Button(screen,text="Four",bg="black",fg="white",height=3,width=5)
btn.grid(row=1,column=1)

screen.mainloop()