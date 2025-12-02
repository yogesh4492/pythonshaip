class A:
    def input(self,num1,num2):
        self.num1=num1
        self.num2=num2
class B(A):
    def display(self):
        print(self.num1)
        print(self.num2)

class C(B):
    def Addition(self):
        print(f"{self.num1} + {self.num2}  = {self.num1+self.num2}")

obj=C()
obj.input(10,20)
obj.display()
obj.Addition()
