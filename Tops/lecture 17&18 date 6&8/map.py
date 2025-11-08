l1=[i for i in range(10,100,10)]

l2=[]

for i in l1:
    l2.append(i+5)
print(l1)
print(l2)
# l2=[]
def myfun(num):
    return num+5


l3=list(map(myfun,l1))
print(l3)


l4=[i+5 for i in l1]
print(l4)