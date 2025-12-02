class A:
    def input(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def display(self):
        print(self.num1)
        print(self.num2)
    
class B(A):
    def Addition(self):
        self.ans=self.num1+self.num2
        print(f"{self.num1} + {self.num2} = {self.ans}")


obj=B()
obj.input(10,20)
obj.display()
obj.Addition()

    
        