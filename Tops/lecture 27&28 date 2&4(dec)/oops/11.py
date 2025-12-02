class A:
    def input(self):
        self.num1=int(input("Enter Number1 = "))
        self.num2=int(input("Enter Number2 = "))
class B(A):
    def Addition(self):
        self.ans=self.num1+self.num2
        # print(ans)
class C(A):
    def Multiplication(self):
        ans=self.num1*self.num2
        print(ans)
class D(B):
    def division(self):
        total=self.ans
        print(total)

objb=D()
objb.input()
objb.Addition()
objb.division()

objc=C()
objc.input()
objc.Multiplication()
