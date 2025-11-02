"""add one set to another add any type data like list and tuple"""

set1={1,2,3,2,111,3}
set2={"hello"}

set1.update(set2)
print(set1)

lis=[32,43,2,3,4]
set1.update(lis)
print(set1)