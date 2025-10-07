string1="python"
print(string1[:])
print(string1[::])
print(string1[::-1])


reverse1=string1[::-1]
if reverse1==string1:
    print("Its PAlindrome")
else:
    print("Its nOt palindrome")

s2='mom'
re_s2=s2[::-1]

if s2==re_s2:
    print("Its PAlindrome")
else:
    print("Its Not a palindrome")