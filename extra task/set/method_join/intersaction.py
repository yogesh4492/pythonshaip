set1={1234,3,1,3,3,2,32}
set2={1,23,323,2,2}

s3=set1 & set2
s4=set1.intersection(set2)

print(s3)
print(s4)


set1.intersection_update(set2)
print(set1)
