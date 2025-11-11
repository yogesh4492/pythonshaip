s1="Python"


"""
----------------------------------
1 | 2 | 3 | 4 | 5 | 6 +ve index
P | y | t | h | o | n
-6|-5 |-4 |-3 |-2 |-1 -ve index


[start:stop:step]

by default +ve start from 0
byn default -ve start from -1

step 1: +ve (it will move forword) ---> (left to right)
step -1 :-ve (it will move backword) <---(right  to left)



"""

s1="PYTHON"

print(s1[-1:1:-1]) 
print(s1[-1:1:1])# empty

print(s1[::-1])