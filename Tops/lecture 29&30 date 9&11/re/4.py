import re

data="my fav language is python"

result=re.search("python",data)
print(result)
print(result.group())