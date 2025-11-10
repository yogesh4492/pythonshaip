# global scope means variable declare globaly not inside any function or ny part of code 

x=300

def myfunc():
    print(x)# this work

myfunc()
print(x)# this is also work with global scope variable

# in below example we use both local and global its give the 

y=10

def my():
    y=20
    print(y)# its print 20 because local value is 20

my()
print(y)# its print 10 because it only access global variable