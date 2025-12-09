class Parent:
    def display(self):
        print("parent class")
class Child(Parent):
    def display(self):
        Parent.display(self)# call parent class 
        print("child class")

obj=Child()
obj.display()