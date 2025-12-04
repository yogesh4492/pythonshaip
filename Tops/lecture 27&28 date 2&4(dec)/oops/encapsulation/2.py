class Student:
    def __init__(self):
        self.name="yogesh" #public
        self.__score=89 #private

    def display(self):
        print(self.name)
        print(self.__score)
    

obj=Student()
print(obj.name)


# print(obj.__score)# not work

obj.display()