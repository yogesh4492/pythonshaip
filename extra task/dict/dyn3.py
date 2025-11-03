student={}
while True:
    sub={}
    student_name=input("Enter Student Name = ")
    student_subject=input("Enter Subject name= ")
    student_score=int(input("Enter Score = "))
    sub['subject']=student_subject
    sub['score']=student_score

    student[student_name]=sub
    choice=input("enter Y For Add More Student= ").lower()
    if choice!='y' and choice!='yes':
        break
print(student)