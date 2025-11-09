# argument and paramener of function

def hello(name):
    print("Hello",name)

#this function only accept one argument of you give more or less argument its raise error

hello("yogesh")# its give hello Yogesh
# hello()# raise error
# hello("yog",'patel') #its also aise error


# default argument in  in the function that noit raise error its not give error

def hello(name="Yogesh"):
    print("HEllo ",name)

hello()# now its print default
hello("Ram") #now its change name to hello ram


# default argument give at as last  argument or parameter of function otherwise its raise error
def hello(ra,name=1):
    print(ra,name)

hello("yogesh","kem") # its take as line wise so must check order atb time passing argument
