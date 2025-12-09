class student:
    def display(self):
        print("This method 1")
    def display(self,name):
        print("this method 2",name)
    
obj=student()
obj.display("yog")


# Note in python method overloading not work properly or 100 %