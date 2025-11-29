def evenNumbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i
for it in evenNumbers(10):
    print(it)