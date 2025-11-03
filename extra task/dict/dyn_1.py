
student={}
while True:
    key=input("Enter key = ")
    value=input("Enter Value= ")

    student[key]=value
    choice=input("Press 'Y' for input More Pairs= ").lower()
    if choice!='y' and choice!='yes':
        break
print(student)