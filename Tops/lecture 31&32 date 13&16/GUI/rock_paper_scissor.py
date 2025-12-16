
# import random
# print("-"*60)

# Menu="""
#      PRESS 1 FOR ROCK
#      PRESS 2 FOR PAPER
#      PRESS 3 FOR SCISSOR

# """
# print(Menu)
# print("-"*60)

# user_choice=int(input("Enter Your Choice= "))

# -------------------------------------------main logic

from tkinter import *
import random

screen=Tk()
screen.geometry("500x500")
screen.title("ROCK PAPER SCISSOR")
screen.config(background="#e3f2fd")

# ----------------------------------------

mychoice=StringVar()
mychoice.set("")
computer=StringVar()
computer.set("")
Options=['ROCK',"PAPER","SCISSOR"]
def Choice(user_choice):
    computer_choice=random.choice(Options)
    try:
        if user_choice=="ROCK":
            if computer_choice=="ROCK":
                    result.set("DRAW")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="PAPER":
                    result.set("Computer Wins")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="SCISSOR":
                    result.set("You Wins")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                # print(computer_choice)
        elif user_choice=="PAPER":
            if computer_choice=="PAPER":
                    result.set("DRAW")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="SCISSOR":
                    result.set("Computer Wins")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="ROCK":
                result.set("You Wins")
                computer.set(computer_choice)
                mychoice.set(user_choice)
                # print(computer_choice)
        elif user_choice=="SCISSOR":
            if computer_choice=="SCISSOR":
                    result.set("DRAW")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="ROCK":
                    result.set("Computer Wins")
                    computer.set(computer_choice)
                    mychoice.set(user_choice)
                    # print(computer_choice)
            elif computer_choice=="PAPER":
                 result.set("You Wins")
                 computer.set(computer_choice)
                 mychoice.set(user_choice)
                #  print(computer_choice)
            

    except Exception as e:
        print(f"Error: {e}")

# ----------------------------------------

result=StringVar()
result.set("PENDING..")
btn=Button(screen,text="ROCK",font=("arial",16,"bold"),height=1,width=10,bg="#009688",fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2,command=lambda:Choice("ROCK"))
btn.place(x=10,y=50)
btn=Button(screen,text="PAPER",font=("arial",16,"bold"),bg="#009688",height=1,width=8,fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2,command=lambda:Choice("PAPER"))
btn.place(x=190,y=50)
btn=Button(screen,text="SCISSOR",font=("arial",16,"bold"),bg="#009688",height=1,width=8,fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2,command=lambda:Choice("SCISSOR"))
btn.place(x=340,y=50)

btn=Button(screen,textvariable=result,font=("arial",16,"bold"),height=1,width=12,bg="#009688",fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2)
btn.place(x=180,y=150)

Lbl=Label(screen,text="YOUR Choice      : ",font=("arial",16,"bold"))
Lbl.place(x=20,y=220)

Lbl=Label(screen,text="COMPUTER Choice  : ",font=("arial",16,"bold"))
Lbl.place(x=20,y=270)

btn=Button(screen,textvariable=mychoice,font=("arial",16,"bold"),height=1,width=12,bg="#009688",fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2)
btn.place(x=240,y=220)
btn=Button(screen,textvariable=computer,font=("arial",16,"bold"),height=1,width=12,bg="#009688",fg="#e3f2fd",activebackground="#e3f2fd",activeforeground="#009688",bd=2)
btn.place(x=240,y=270)


screen.mainloop()

