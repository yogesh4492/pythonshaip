even=[]
odd=[]
for i in range(5):
    num=int(input("Enter Number= "))
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even Numbers = {even}")
print(f"odd Numbers = {odd}")
