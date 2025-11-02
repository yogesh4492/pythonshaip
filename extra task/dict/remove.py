dict1={
    'name':'yogesh',
    'subject':'python',
    'score':99,
    'year':2025
}
print(dict1)
dict1.pop('name')#want key
print(dict1)

dict1.popitem()# remove last
print(dict1)

dict1.clear()
print(dict1)
del dict1
# print(dict1) error keyerror
