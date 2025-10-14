"""
pop() its remove element by specific index

"""

fruits_list=['apple','banana','grapes','orange','mango']
print(fruits_list)
print(len(fruits_list))

index_value=int(input("Enter Index Value= "))
if index_value>=0 and index_value<len(fruits_list):
    res=fruits_list.pop(index_value)
    print(f"{res} Remove Succesfuuly")
    print(fruits_list)
else:
    print("Index Position Does Not Exists!!!")