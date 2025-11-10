# scope : a variable is only available from inside the region itsis created this is called scope

# local scope : 
#  a variable created inside a function belongs tot he local scope of that function and can 
#  only be used inside that function 
# scope of x only inside function we are not able to access x outside function but also used in inside function
def myfunc():
    x=300
    def myfunc1():
        print(x)
    myfunc1()

myfunc()
# print(x) its not abl to access outside so this statement raise error
# myfunc1()