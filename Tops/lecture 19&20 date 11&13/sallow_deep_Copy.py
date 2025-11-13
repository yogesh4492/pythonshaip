l1=[10,20,30]

l2=l1

l2.append(40)
print(l1)
print(l2)


# shallow copy tha t store address means its also copy the value and address 
# change that affect original list

a1=[10,20,30]
a2=a1.copy()
a2.append(40)
print(a1)
print(a2)

# deep copy that only copy value that not affect original list

