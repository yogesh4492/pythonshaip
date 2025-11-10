# using global keyword before the variable name we can set it global even if used inside function

def myname():
    global x# its used to access global variable and also to create global variable
    x=100
    print(x)

myname()
print(x)




