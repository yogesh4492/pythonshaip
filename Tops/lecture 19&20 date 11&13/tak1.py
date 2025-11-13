"""
accept 5 subject from user
just filter out those function name which
"""

l1=[]
for i in range(5):
    name=input("Enter  subject= ")
    l1.append(name)

l2=list(filter(lambda subject:len(subject)>6,l1))
print(l2)