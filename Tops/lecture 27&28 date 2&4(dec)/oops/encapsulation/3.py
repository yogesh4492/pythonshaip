class Product:
    def __init__(self):
        self.mobile=15000
        self.__laptop=25000

    def display(self):
        print(f"Mobile : {self.mobile}")
        print(f"Laptop : {self.__laptop}")
    
    def changePrice(self,newPrice):
        self.__laptop=newPrice

obj=Product()

obj.display()

obj.mobile=25000

obj.display()

obj.__laptop=70000# not giv error but its not change value
obj.display()
print("-"*10)

obj.changePrice(7000)
obj.display()