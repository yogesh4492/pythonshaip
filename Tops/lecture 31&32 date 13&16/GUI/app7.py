from tkinter import * 


screen =Tk()

screen.geometry("500x500")
# tkinter variable 

visibletext=StringVar()
visibletext.set("PENDING")


def userchoice(choice):
    global visibletext
    visibletext.set(choice)


btn1=Button(screen,text="ROCK",font=('arial',16,"bold"),bg="teal",fg="white",command=lambda:userchoice("ROCK"))
btn1.place(x=10,y=50)
btn1=Button(screen,text="PAPEr",font=('arial',16,"bold"),bg="teal",fg="white",command=lambda:userchoice("paper"))
btn1.place(x=160,y=50)
btn1=Button(screen,text="SCissor",font=('arial',16,"bold"),bg="teal",fg="white",command=lambda:userchoice("scissor"))
btn1.place(x=310,y=50)

btn1=Button(screen,textvariable=visibletext,font=('arial',16,"bold"),bg="teal",fg="white")
btn1.place(x=160,y=150)

screen.mainloop()

