import random

print(f"Random From 1 To 10 : {random.randint(1,10)}")
print(f"Random By default from 0 to 1 ::{random.random()}")
print(f"OTP example :: {random.randint(1111,9999)}")

l1=['python','java','ds','da']

print(f"RAndom From Specofic list:: {random.choice(l1)}")
print(f"Random from specific character set::{random.choice('python')}")