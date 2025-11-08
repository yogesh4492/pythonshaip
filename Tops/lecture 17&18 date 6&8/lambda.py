"""
lambda function:
 -ananymous function

 - function with out any name
 - function can accept many parameters but there only one return value or one statement
 - using of lambda keyword we can define lambda function



"""

# with out lambda

def addition(n1,n2):
    return n1+n2

print(addition(10,20))

#with lambda

ans=lambda num1,num2: num1+num2
print(ans(10,25))