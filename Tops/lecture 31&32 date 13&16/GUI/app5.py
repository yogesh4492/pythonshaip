from tkinter import *

screen=Tk()
screen.title("Counter app")
screen.geometry("300x400")
screen.config(background="black")

# python varible
count=0
tv_price=0

# tkinter variable 
count_tk=IntVar()
count_tk.set(count)

total_tk=IntVar()
total_tk.set(tv_price)


def increment():
    global count,count_tk,total_tk,tv_price
    count+=1
    count_tk.set(count)

    tv_price=15000*count
    total_tk.set(tv_price)

def decrement():
    global count,count_tk,total_tk,tv_price
    if count>0:

        count-=1
        count_tk.set(count)

        tv_price=15000*count
        total_tk.set(tv_price)
    


lbl1=Label(screen,text="TV = 15000",font=('arial',26))
lbl1.pack()

btn1=Button(screen,text="+",height=2,width=8,command=increment)
btn1.place(x=10,y=50)
btn1=Button(screen,text="-",height=2,width=8,command=decrement)
btn1.place(x=170,y=50)
lbl1=Label(screen,textvariable=count_tk,font=('arial',26))
lbl1.place(x=30,y=220)
lbl1=Label(screen,textvariable=total_tk,font=('arial',26))
lbl1.place(x=30,y=320)

screen.mainloop()