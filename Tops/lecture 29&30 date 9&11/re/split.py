import re

data="apple,banana;mango"
data=re.split(r"[;,]",data)
print(data)