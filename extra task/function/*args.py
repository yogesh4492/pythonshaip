# by default a function must be called with correct number of arguments.
# however sometimes you may not kno how many arguments that will be passed into your function
# for that cases we use *args and **kwargs  that accept unknown number of argumets

# arbitrary Argumenrs - *args  : tuple as argument
# This way, the function will receive a tuple of arguments and can access the items accordingly:
# if you do not know how many arguments will be passed into your function add a * before the parameter name.

def myname(*kids):
    print(kids)
    print("Type : ",type(kids))
    for i in kids:
        print(i)

myname('Yogesh','ram','krishna')

#normal argument with the normal argument

def myfunc(greetings,*a):
    print(len(a))
    for i in a:
        print(greetings,"!!, ",i)

myfunc("hello",'yogesh','ram','rohit','rahul')


l1=[x for x in range(1,101)]
tu=tuple(l1)
# print(tu)
def sump(*a):
    sum=0
    for i in a:
        sum+=i
        
    return sum
#unpacking 
# sump(*tu)
print("sum Of 1 To 100 numbers is = ",sump(*tu))
print("")