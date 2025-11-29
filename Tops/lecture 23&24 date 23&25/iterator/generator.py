# def test():
#     return 1
#     return 2

def test():
    yield 1
    yield 2


it=iter(test())
print(next(it))
print(next(it))
# print(next(it))raise stopitration error


