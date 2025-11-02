dict={
    'name':'yogesh',
    'subject':'python',
    'score':95
}
# change existing 
print(dict)
if 'score' in dict:
    dict['score']=99
print(dict)

# using update method
dict.update({'nam':'ram'})
print(dict)
# add new
dict['year']=2025
print(dict)

