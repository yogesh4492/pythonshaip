

import random

computer=random.randint(1,100)

flag=True
#level one 
print("Welcome in Number Guessing Game ")
level1=True
if level1:
        
    while flag:
        Your=int(input("Guess Number= "))
        if Your>computer:
            print("Hint : Guess Lower Number")
        elif Your<computer:
            print("Hint : Guess High Number")
        else:
            print("Right Choice!!")
            flag=False
            level1=False
            level2=True
    flag=True
    if level2:
        while flag:
            your=int(input("Enter The number= "))



