import os
class Main:
    def welcome_fun(self):
        print("".center(55,"*"))
        print("welcome in Repair Order Booking System".center(55,"*").upper())
        print("".center(55,"*"))
    def thanks_fun(self):
        print("".center(55,"*"))
        print("thank you for visiting...".center(55,"*").upper())
        print("".center(55,"*"))

    def booking(self):
            self.data={}

            while True:
                self.customer_name=input("Enter Customer Name : ".title())
                self.device_type=input("enter device type : ".title())
                self.issue=input("Enter Wht is issue in Device : ".title())
                self.due_date=input("enter Due Date Of repairing : ".title())
                self.sub={}
                self.sub['device_type']=self.device_type
                self.sub['issue']=self.issue
                self.sub['due_date']=self.due_date
                self.data[self.customer_name]=self.sub
                ch=input("Press 'Y' To add More Customer Detail .... : ").lower()
                if ch!="y":
                    print(self.data)
                    break
            return self.data
                
    def parts(self,data):
        sub={}
        sum=0
        while True:
            self.part_name=input("Enter the part name : ")
            self.part_price=int(input("Enter the part price : "))
            self.sum+=self.part_price
            sub[self.part_name]=self.part_price
            ch=input("Press Y to add more parts ....").lower()
            if ch!="y":
                break
        if self.cus in data:
            self.data[self.cus]['parts']=sub
        return data,sum
    
    def read_file(self):
        if os.path.exists(f"{self.customer_name}.txt"):
            with open(f"{self.customer_name}.txt","r") as f:
                data=f.read()
                return data
    def write_file(self):
        with open(f"{self.customer_name}","a") as f:
            f.wrire(self.data)

    def invoice(self):
        name=input("Enter customer name...: ")
        data=self.read_json()
        if name in data:
            choice=input("Do You Want To add parts Detail of it ... press 'P' for add parts : ".title()).lower()
            if choice=="p":
                dat,total=self.parts(data,name)
                print(dat,total) 
            return dat,total       
        else:
            print("Please check detail user is not exist...")

    def run(self):
        self.welcome_fun()
        menu="""
                A) Press 1 for check Existing Record
                B) press 2 for add new customer details and parts details
                C) press 3 for make invoice
            """ 
        print(menu.title())
        while True:
            choice=int(input("Enter Your Choice ..."))
            if choice==1:
                self.cus=input("Enter Customer Name : ")

                if os.path.exists(f"{self.cus}.txt"):
                    data=self.read_file()
                    # data=pd.read_json("data.json")
                    if not data:
                        print("no data in json file")
                    else:
                        print(data)
                    # data=read_json()
                    # print(data)
                else:
                    print("No json file detected")

            elif choice==2:
                global book
                book=self.booking()
                # dump_json(book)
            elif choice==3:
                d,t=self.invoice()
        
            ch=input("Press Y to perform more operation... ").lower()
            if ch!="y":
                break
            else:
                pass

    # def main():
    #     try:
    #         welcome_fun()
    #         menu="""
    #                 A) Press 1 for check Existing Record
    #                 B) press 2 for add new customer details and parts details
    #                 C) press 3 for make invoice
    #             """ 
    #         print(menu.title())
    #         while True:
    #             choice=int(input("Enter Your Choice ..."))
    #             if choice==1:
    #                 if os.path.exists("data.json"):
                    
    #                     data=read_json()

    #                     # data=pd.read_json("data.json")
    #                     if not data:
    #                         print("no data in json file")
    #                     else:
    #                         print(data)
    #                     # data=read_json()
    #                     # print(data)
    #                 # else:
    #                 #     print("No json file detected")

    #             elif choice==2:
    #                 global book
    #                 book=booking()
    #                 # dump_json(book)
    #             elif choice==3:
    #             d,t=invoice()
    #             dump_json(d)
    #             ch=input("Press Y to perform more operation... ").lower()
    #             if ch!="y":
    #                 break
    #             else:
    #                 pass

    #     except FileNotFoundError as e:
    #         print(f"Error Message: {e}")
    #     finally:

    #         # print("Thank You")


obj=Main()
obj.run()    

