"""function with parameter ansd with return type"""

mobile=10
laptop=20

Mobile_price=25000
laptop_price=40000

def product(product,qty):
    global mobile,laptop,laptop_price,Mobile_price
    if product=="Mobile":
        total=qty*Mobile_price
        discount=total*mobile/100
        net=total-discount
        return net
    elif product=="laptop":
        pass
    else:
        print("Invalid Product")


product_name=input("Enter Name Of Product Category ==")
qty=int(input("Enter Quantity For Buy= "))

print("Total Amount To Pay = ",product(product_name,qty))