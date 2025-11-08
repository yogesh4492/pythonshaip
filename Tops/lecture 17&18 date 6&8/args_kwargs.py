"""
*args and **kwargs


*args = arguments |tuple as parameter
**kwargs = key with arguments | dict as parameter



"""


def sum(*a):
    result=0
    print(len(a))
    for i in a:
        result+=i
    print(result)

sum(10,20,30)