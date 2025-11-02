tu=[1]
print(tu,type(tu))
tuple1=(1,0)
print(tuple1,type(tuple1))


print(tuple1[1])
for i in tuple1:
    print(i)

tu[0]=10
print(tuple1)
print(tu)




li=list(tuple1)

li[0]=50
tuple1=tuple(li)
print(tuple1)
tup=(12,)
tuple1+=tup
print(tuple1)
# tuple1.clear()
del tuple1
print(tuple1)