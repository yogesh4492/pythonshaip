from abc import ABC,abstractmethod

class Parent(ABC):
    @abstractmethod
    def display():
        pass

class A(Parent):
    def display(self):
        print("Class A here")
class B(Parent):
    def display(self):
        print("class B here")


a=A()
b=B()
a.display()
b.display()


