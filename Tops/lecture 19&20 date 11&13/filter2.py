
l1=["a",'e','b','c','d']

l2=list(filter(lambda char:char.upper() in 'AEIOU',l1))

print(l2)
