import re

data="Ram Patel Have python subject and Shrey patel have java subject"
result=re.findall(r"\b[A-Z][a-z]*\b",data)
print(result)