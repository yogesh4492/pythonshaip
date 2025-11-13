""" 
filter : filter is function that filter value from sequence or itretor  
  


syntax:
    filter(function,sequence)


"""


list1=[1,2,3,4,4,25,7,56]

# using without any methid normally
l2=[]
def myfunc():
    for i in list1:
        if i%2==0:
            l2.append(i)
myfunc()
print(l2)

# using filter and lambda

l3=list(filter(lambda num:num%2==0,list1))
print(l3)
# using list comprehension

l4=[i for i in list1 if i %2==0]
print(l4)

