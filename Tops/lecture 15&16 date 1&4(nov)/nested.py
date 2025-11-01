student={}

status=True
while status:
    sub={}
    student_name=input("Enter Student= ")
    subject_name=input("Enter Sub= ")
    score=int(input("Enter Score= "))

    sub['subject_name']=subject_name
    sub['score']=score

    student[student_name]=sub
    print(student)

    choice=input("Enter Y for Continue= ").lower()
    if choice!='y' and choice!='yes':
        status=False
