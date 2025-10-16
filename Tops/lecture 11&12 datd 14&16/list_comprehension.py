"""
List Comprehension : Its Shorter Way To Create A list
"""

#without list comprehension

l=[]
for i in range(1,6):
    l.append(i)

print(l)
print("-"*20)
# with list comprehension
#  2      1
# value  loop


l1=[x for x in range(1,6)]

print(l1)