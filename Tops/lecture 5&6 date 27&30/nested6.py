"""
A
B C
D E F 
G H I J

"""
num=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num+=1
    print()