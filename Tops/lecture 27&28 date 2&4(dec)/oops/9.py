class A:
    def displayA(self):
        print("class A here...")
class B(A):
    def displayB(self):
        print("class B here...")
class C(A):
    def displayC(self):
        print("class C here...")

objb=B()
objb.displayA()
objb.displayB()

objc=C()
objc.displayA()
objc.displayC()