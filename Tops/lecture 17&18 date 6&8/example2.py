"""
function with parameter and withoput return type"""

def add(n1,n2):
    ans=n1+n2
    print("ans =",ans)
def mul(n1,n2):
    ans=n1*n2
    print("Ans= ",ans)
def div(num1,num2):
    ans=num1/num2
    print("Ans= ",ans)
def sub(num1,num2):
    ans=num1-num2
    print("Ans=",ans)


menu="""
          Press1 for addition 
          press 2 for multiplication
          press 3 for division
          press 4 for subtraction


"""
print(menu.upper())
while True:
    choice=int(input("Enter Your Coice= "))
    num1=int(input("Enter Num1= "))
    num2=int(input("Enter Num2= "))

    if choice==1:
        add(num1,num2)
    elif choice==2:
        mul(num1,num2)
    elif choice==3:
        div(num1,num2)
    elif choice==4:
        sub(num1,num2)
    else:
        print("Invalid Choice")
    ch=input("Press Y For Perform More Operation == ").lower()
    if ch!='y' and ch!='yes':
        break