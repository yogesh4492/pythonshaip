class A:
    def displayA(self):
        print("cklss A here...")
class B:
    def displayB(self):
        print("cklss B here...")
class C(A,B):
    def displayc(self):
        print("cklss C here...")
        
        
obj=C()
obj.displayA()
obj.displayB()
obj.displayc()