list1=[1,2,3,34,4]
print(list1,len(list1))
a,*b=list1
print(a,b)

tuple1=(23,43,22,3,43,4,2,2,2,76)
print(tuple1,len(tuple1))

(k,*p)=tuple1
print(k,p)
