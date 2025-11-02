dict={
    'name':'yogesh',
    'subject':'python',
    'score':90
}

print(dict)
print(len(dict))
print(dict['name'])
print(dict['subject'])
print(dict['score'])
# print(dict['year':'2024'])
dict['year']=2025
print(dict.get('year'))

print(dict.keys())
print(dict.items())
print(dict.values())
for i in dict:
    print(i)
