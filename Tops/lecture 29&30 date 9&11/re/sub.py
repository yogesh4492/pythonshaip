# replqace text 

import re
data="my conntact number is 9537638715"

data=re.sub(r"9537638715","9106938715",data)
print(data)

# mask phone number 

data = re.sub(r"\d{6}(\d{4})", "******\\1", data)
print(data)

data="my adhar numbeer is 535380912356"
data=re.sub(r"\d{8}(\d{4})","*******\\1",data)
print(data)