s1='hello python'
status=False
no_vowel=0
for i in s1:
    if i in 'aeiou':
        status=True
        no_vowel+=1
print(status)
print(f"No of Vowel In string is {no_vowel}")
