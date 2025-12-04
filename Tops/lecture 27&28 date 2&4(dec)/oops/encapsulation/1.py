class Student:
    def __init__(self,name,subject,score):
        print("Welcome to student class".upper())
        self.name=name
        self.score=score
        self.subject=subject
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setscore(self,score):
        self.score=score
    def getscore(self):
        return self.score
    def setsubject(self,subject):
        self.subject=subject
    def getsubject(self):
        return self.subject
obj=Student("yogesh","python",78)
print(obj.getname())
obj.setscore(99)
print(obj.getscore())
    