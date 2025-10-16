"""  combine two lisyt in one"""

l1=['vadapav','dabeli','sandwich','meggi']
l2=[1,23,43,23]
l3=[(x,y) for x in l1 for y in l2]
print(l3)
print(len(l3))