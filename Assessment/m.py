import json
import pandas as pd
import os


def welcome_fun():
    print("".center(55,"*"))
    print("welcome in Repair Order Booking System".center(55,"*").upper())
    print("".center(55,"*"))

def booking():
    try:
        data={}

        while True:
            customer_name=input("Enter Customer Name : ".title())
            device_type=input("enter device type : ".title())
            issue=input("Enter Wht is issue in Device : ".title())
            due_date=input("enter Due Date Of repairing : ".title())
            sub={}
            sub['device_type']=device_type
            sub['issue']=issue
            sub['due_date']=due_date
            data[customer_name]=sub
            ch=input("Press 'Y' To add More Customer Detail .... : ").lower()
            if ch!="y":
                print(data)
                break
        return data
    except:
        print("something wrong in booking")
            
        
def thanks_fun():
    print("".center(55,"*"))
    print("thank you for visiting...".center(55,"*").upper())
    print("".center(55,"*"))

def parts(data,cus_name):
    sub={}
    sum=0
    while True:
        part_name=input("Enter the part name : ")
        part_price=int(input("Enter the part price : "))
        sum+=part_price
        sub[part_name]=part_price
        ch=input("Press Y to add more parts ....").lower()
        if ch!="y":
            break
    data[cus_name]['parts']=sub
    return data,sum
    


def dump_json(data):
    with open("data.json","a") as j:
        json.dump(data,j,indent=4)

def read_json():
    with open("data.json","r") as j:
        return json.load(j)

def invoice():
    name=input("Enter customer name...: ")
    data=read_json()
    if name in data:
        choice=input("Do You Want To add parts Detail of it ... press 'P' for add parts : ".title()).lower()
        if choice=="p":
            dat,total=parts(data,name)
            print(dat,total) 
        return dat,total       
    else:
        print("Please check detail user is not exist...")


def main():
    try:
        welcome_fun()
        menu="""
                A) Press 1 for check Existing Record
                B) press 2 for add new customer details and parts details
                C) press 3 for make invoice
            """ 
        print(menu.title())
        while True:
            choice=int(input("Enter Your Choice ..."))
            if choice==1:
                if os.path.exists("data.json"):
                
                    data=read_json()

                    # data=pd.read_json("data.json")
                    if not data:
                        print("no data in json file")
                    else:
                        print(data)
                    # data=read_json()
                    # print(data)
                # else:
                #     print("No json file detected")

            elif choice==2:
                global book
                book=booking()
                # dump_json(book)
            elif choice==3:
               d,t=invoice()
               dump_json(d)
            ch=input("Press Y to perform more operation... ").lower()
            if ch!="y":
                break
            else:
                pass

    except FileNotFoundError as e:
        print(f"Error Message: {e}")
    finally:
        thanks_fun()
        # print("Thank You")


if __name__=="__main__":
    main()
    

