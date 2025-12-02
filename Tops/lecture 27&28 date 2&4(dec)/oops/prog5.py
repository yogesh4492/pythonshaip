class A:
    def displayA(self):
        print("Class A here...")
class B(A):
    def displayB(self):
        print("Class B here....")

#always object create of derived or child classs

obj=B()
obj.displayA()
obj.displayB()