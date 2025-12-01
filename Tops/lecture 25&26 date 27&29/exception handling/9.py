
class AgeException(Exception):
    pass

try:
    age=int(input("Enter Your age: "))
    if age<=18:
        raise AgeException("User below 18 not allowed")
    else:
        print("Welcome")
except AgeException as e:
    print("Mesaage : ",e)