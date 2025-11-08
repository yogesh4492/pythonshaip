"""
**kwargs : key with arguments | dictionary as a parameter

"""

def student(**kwargs):
    for name,score in kwargs.items():
        print(f"{name} : {score}")

student(yogesh=10,yash=20,jay=30)
