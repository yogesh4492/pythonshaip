set1={'apple','banana','kiwi'}
set2={'banana','orange','mango'}
#diuffrence that only in set one not in set 2
s3=set1.difference(set2)
s4=set2-set1
print(s3)
print(s4)
set1.difference_update(set2)
print(set1)