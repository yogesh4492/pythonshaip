class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class child(Parent):
    def __init__(self,name,subject):
        Parent.__init__(self,name)
        self.subject=subject
    def display(self):
        Parent.display(self)
        print(self.subject)

obj=child("Yogesh","Python")
obj.display()