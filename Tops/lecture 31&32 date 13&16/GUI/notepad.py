from tkinter import *
from tkinter import filedialog
screen=Tk()

screen.geometry("600x600")
screen.title("Yogesh PAtel Notepad")
text_Area=Text(screen)
text_Area.pack(expand=True,fill="both")

# -----------------main logic

def new():
    # global text_Area
    text_Area.delete("1.0","end")


def openfun():
    file_path=filedialog.askopenfilename(
        filetypes=[("text files","*.txt"),("all files","*.*")]
    )
    with open(file_path,"r") as f:
        context=f.read()
    text_Area.insert("1.0",context)

# -----------------------------------
menu_bar=Menu(screen)
screen.config(menu=menu_bar)


file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="FIle",menu=file_menu)

HElp_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="HELP",menu=HElp_menu)
about_us_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="About Us",menu=about_us_menu)

# --------------------------------

file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=openfun)
file_menu.add_command(label="SAve")

file_menu.add_separator()

file_menu.add_command(label="Exit")

screen.mainloop()