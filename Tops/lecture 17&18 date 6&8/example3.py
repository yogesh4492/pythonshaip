"""function without parameter and return type"""


def findfactorial():
    num=int(input("Enter Number= "))
    f=1
    for i in range(1,num+1):
        f*=i
    return f

ans=findfactorial()
print("Factorial =",ans)
