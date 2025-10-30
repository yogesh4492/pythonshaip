# Remove duplicates from a list using set().

list1=[1,2,3,222,2,2,43,3,1]
unique=set(list1)
# rm_dup=list(unique)
print(list(unique))

from collections import Counter
cou=Counter(list1)
print(cou)
