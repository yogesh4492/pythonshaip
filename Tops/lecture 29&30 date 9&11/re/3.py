import re
data="my fav language is python"

result=re.match("python",data)
print(result)
data1="python is my fav programming langauge"
result=re.match("python",data1)
print(result)
print(result.group())