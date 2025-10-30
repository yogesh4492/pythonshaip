student={
    "name":'yogesh',
    'subject':'python',
    "score":90
}


for i in student.keys():
    print(i)
for j in student.values():
    print(j)
for i,j in student.items():
    print(f"{i} = {j}")
for i in student:
    print(i)