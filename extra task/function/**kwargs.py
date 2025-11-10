# arbitary keyword Arguments - **kwargs

# if you do not know how many keyword argumnets will be passes inot your function add two asterisks ** befor the parameter name

# this way,the function will receieva dictionary as argument

def myfunc(**kids):
    print("his First Name is ",kids.get('fname'))
    print("His last name is ",kids.get('lname'))
    for i in kids:
        print(i , kids[i])
myfunc(fname='Yogesh',lname='Patel')


# unpacking dictionary  with it

mydict={'name':'yogesh','score':99}

# myfunc(mydict) without unpacking its give error

#  so use the same ** at time of calling

myfunc(**mydict)