# num1=int(input("Enter A number : "))
# num2=int(input("Enter A number : "))

# div=num1/num2

# print(div)

try:
    num1=int(input("Enter Num1= "))
    num2=int(input("Enter Num2= "))
    ans=num1/num2
    # print(ans)

except ValueError:
    print("please enter valid input !")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(ans)