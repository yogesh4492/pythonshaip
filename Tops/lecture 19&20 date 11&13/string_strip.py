s1="python"
print(s1)


s1="   python    "
print(len(s1))


# strip : strip method remove whitespace from the leading and traling string
print(s1.strip())
# repr method that reperesent string in single quotes

s1="   python   "
print(repr(s1))
s1=s1.strip()
print(repr(s1))
#lstrip: lstrip remove whitespace from leading or starting


s1="   python   "
print(repr(s1))
s1=s1.lstrip()
print(repr(s1))

# rstrip : rstrip remove whitespace from traling or ending


s1="   python   "
print(repr(s1))
s1=s1.rstrip()
print(repr(s1))