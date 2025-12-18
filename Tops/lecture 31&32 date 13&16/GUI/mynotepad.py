from tkinter import *
from tkinter import filedialog

screen=Tk()
screen.title("Yogesh Patel Notepad")
screen.geometry("1000x1000")
screen.config(background="#1E1E1E")

text_Area=Text(screen,bg="#252526",fg="#D4D4D4",font=('arial',16,"bold"))
text_Area.pack(expand=True,fill="both")
text_Area.config(insertbackground="white")
menu_bar=Menu(screen)
screen.config(menu=menu_bar,background="#252526")

# -----------------------------------
#main logic 

def new(event=None):
    text_Area.delete("1.0","end")

def fileopen(event=None):
    file_path=filedialog.askopenfilename(
        filetypes=[("text files","*.txt"),("all files","*.*")]
    )
    with open(file_path,"r") as r:
        data=r.read()
    text_Area.insert("1.0",data)
def save(event=None):
    data=text_Area.get("1.0","end")
    file_name=filedialog.asksaveasfilename(
        filetypes=[("text files","*.txt"),("All files","*.*")]
    )
    with open(file_name,"w") as write:
        write.write(data)
# -----------------------------------

file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="FILE",menu=file_menu)

Help_Menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="HELP",menu=Help_Menu)

ABOUT_US=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="ABOUT US",menu=ABOUT_US)

file_menu.add_command(label="NEW",command=new)
file_menu.add_command(label="OPEN",command=fileopen)

file_menu.add_command(label="SAVE",command=save)
file_menu.add_separator()
file_menu.add_command(label="EXIT",command=exit)


screen.mainloop()

