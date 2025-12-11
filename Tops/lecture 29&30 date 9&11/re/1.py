import re

data=" My contact no is 9537638715"
data2="Ram is 20 years old , jay is 30 years old , neha is 16 years old."
result=re.search(r"\d{10}",data)
print(result.group())

result=re.findall(r"\d{10}",data)
print(result)

result2=re.findall(r"\d{2}",data2)
print(result2)