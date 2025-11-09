# function without return type and withput parameter

def gretings():
    print("Hello Good Morning!!")

# if __name__=="__main__":
gretings()

# with parameer ans without return type

def add(n1,n2):
    print(f"addition of {n1} and {n2} is ={n1+n2}")

add(10,20)


# without parameter and with return type

def mul():
    n1=int(input("Enter Number1= "))
    n2=int(input("Enter Number2= "))
    return n1*n2

print(mul())


# with pameter and with return tyoe


def div(n1,n2):
    return n1//n2

print("10 divide by 2 = ",div(10,2))
    
    
