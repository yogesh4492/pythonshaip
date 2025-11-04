"""
Date 4-11-2025


"""
print("-"*55)
print("Welocme In Grocery Shop".center(55,'-'))
print("-"*55)

product={}
while True:
    menu="""
    press 1 for manager roll
    press 2 for customer roll
    """
    print(menu)
    user_roll=int(input("Enter User Roll = "))
    
    if user_roll==1:

        print("Welcome To Manager Panel")
        while True:
            option="""
        
                press 1 for add product
                press 2 for view product
                press 3 for remove product(only one product at time)

            """
            print(option)
            choice=int(input("Enter Your Choice= "))
            if choice==1:

                while True:
                    sub={}

                    product_name=input("Enter Product Name = ")
                    product_qty=int(input("Product Quantity= "))
                    product_price=float(input("Enter Product Price= "))

                    if product_name in product.keys():
                        sub['qty']=product_qty+product[product_name].get('qty')
                        sub['price']=product_price
                    else:
                        sub['qty']=product_qty
                        sub['price']=product_price
                    product[product_name]=sub
                    # print(product)

                    choice=input("Press Y For Add More Items = ").lower()
                    if choice!='y' and choice!='yes':
                        break
            elif choice==2:
                for i in product.keys():
                    print(f"{i}    | Qty.  {product[i]['qty']}   | Price .  {product[i]['price']}")
            elif choice==3:
                inq=input("Enter Product name for remove= ")
                if inq in product.keys():
                    print(product.pop(inq),"Remove successfully")
                    
                else:
                    print("Product Not In product list")
            else:
                print("Invalid Option")
            choice=input("Press Y for Continue in MAnager Panel  = ").lower()
            if choice!='y' and choice!='yes':
                break
            
    elif user_roll==2:
        print("Welcome To customer Panel ")
        while True:
            option="""
                    press 1 for view Product
                    press 2 for Buy Product

            """
            print(option)

            choice=int(input("Enter Your Choice= "))
            if choice==1:
                print("hello")
                for i in product.keys():
                    print(f"{i}    | Qty.  {product[i]['qty']}   | Price .  {product[i]['price']}")
            elif choice==2:
                product_name=input("Enter Product name= ")
                product_qty=int(input("Enter Product Qty for Buy= "))
                
                if product_name in product.keys():
                    amount=product[product_name].get('price')
                    # print(product_qty,'|',product[product_name]['qty'])
                    if product_qty<=product[product_name].get('qty'):
                        total_amount=amount*product_qty
                        product[product_name]['qty']-=product_qty
                        print("Amount To PAy =",total_amount)

                        print()
                        print("Remaining Stock is .....")
                        print()
                        for i in product.keys():
                            print(f"{i}    | Qty.  {product[i]['qty']}   | Price .  {product[i]['price']}")

                    else:
                        print("Sorry Stock Are not available")
                else:
                    print("Product Is Not Avialable")

            choice=input("Press Y For Continue In 'Customer' Panel = ").lower()
            if choice!='y' and choice!='yes':
                break
    else:
        print("Invalid User Roll..")
    cho=input("Press 'Y' For Continue In System = ").lower()
    if cho!='y' and cho!='yes':
        break