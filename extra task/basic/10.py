"""Rectngle Prism Formula 
:2(wl+lh+hw)"""

width=float(input("Enter width= "))
length=float(input("Enter Length= "))
height=float(input("Enter Height= "))
print(f"Height= {height} , Width= {width} length={length}.".upper())
prism=2*((width*length)+(width*height)+(height*length))
print(f"Rectange Prism ={prism}")