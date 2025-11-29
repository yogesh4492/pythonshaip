""" exception handling """
#keyerror

product ={
    "mobile":"vivo",
    "qty":20,
    "price":15000
}
try:
    print(product)
    name=input("Enter product name which you want to check in detailed: ")
    print(product[name])
except KeyError:
    print("Invalid Key")
finally: 
    print("Thank you for using this app ")
    