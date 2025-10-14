menu="""   
                 Menu
        1) Add record 
        2) Remove Record 
        3) View record 

   """
print(menu)
product_list=[]
status=True
while status:

    choice=int(input("Enter your Choice= "))
    if choice==1:
        product=input("Enter Product :::")
        if product in product_list:
            print(f"{product} is already exists")
        else:
            product_list.append(product)
            print("Product Added Successfully!!")
    elif choice==2:
        product=input("Enter Product You Wnat to Remove = ")
        if product in product_list:
            product_list.remove(product)
            print("Productb Remove Succesfully")
        else:
            print("Prfoduct Does Not Exists")
    elif choice==3:
        print("record".center(50,"="))
        for i in product_list:
            print(i)
    else:
        print("Invalid Choice !!")
    
    choic =input("Do You Want To Perform More Operation  Press 'y' for Yes and Press 'n' for No ::   ").lower()
    if choic=='n' or choic=='no':
        status=False
