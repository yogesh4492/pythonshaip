""" Map Function is used as same time calling function and passing value as iterators """

l1=[12,23,43,54,5]

"""
with normal function
"""

l2=[]
def myfun(num):
    return num+5

l2=list(map(myfun,l1))
print(l2)

"""with lambda function"""

l3=list(map(lambda num:num+5,l1))
print(l3)
