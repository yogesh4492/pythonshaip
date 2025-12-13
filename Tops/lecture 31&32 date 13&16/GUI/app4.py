from tkinter import *

screen=Tk()
screen.geometry("500x500")
screen.config(background="#8c9eff")
screen.title("my app")


btn=Button(screen,height=2,width=8,text="PYTHON",font=("arial",16,"bold"),bg="#7c4dff",fg="white",activebackground="#1a237e",activeforeground="white")
btn.place(x=10,y=10)


btn=Button(screen,height=2,width=15,text="DATA SCIENCE",font=("arial",16,"bold"),bg="#7c4dff",fg="white",activebackground="#1a237e",activeforeground="white")
btn.place(x=150,y=10)

screen.mainloop()
