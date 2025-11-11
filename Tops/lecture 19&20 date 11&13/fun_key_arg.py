""" function keyword arguments"""

def student(name,subject):
    print(f"name= {name} subject= {subject}")

student(name="yoigesh",subject="python")


"""function with default argument"""

def student(name,subject="java"):
    print(f"name= {name} subject= {subject}")

student(name="yoigesh",subject="python")
student(name="yoigesh")

