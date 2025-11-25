class student:
    id =1
    name=""

    def input(self,id,name):
        self.id=id
        self.name=name
    
    def display(self):
        print(f"id ={self.id}  subject = {self.name}")

obj=student()


obj.input(1,"AAA")
obj.display()

obj2=student()

obj2.input(2,"BBB")
obj2.display()