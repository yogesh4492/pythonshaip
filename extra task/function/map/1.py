# map function 
# map its use to call function and get value for all iteration
# using map and list comphrehension work same but for more data use map becaue its memory friendly

# without map

main_list=[x for x in range(0,101,10)]
print(main_list)
square_list=[]
for i in main_list:
    square_list.append(i*i)
print(square_list)

# using map

def square(n):
    return n*n

sq=list(map(square,main_list))
print(sq)

# using list comprehension

sq1=[x*x for x in main_list]
print(sq1)