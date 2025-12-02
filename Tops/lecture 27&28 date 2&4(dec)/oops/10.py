class A:
    def input(self):
        self.num1=int(input("Enter Number1 = "))
        self.num2=int(input("Enter Number2 = "))
class B(A):
    def Addition(self):
        ans=self.num1+self.num2
        print(ans)
class C(A):
    def Multiplication(self):
        ans=self.num1*self.num2
        print(ans)

objb=B()
objb.input()
objb.Addition()

objc=C()
objc.input()
objc.Multiplication()
