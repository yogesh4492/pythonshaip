""" take subject and store in file"""


f=open("myfile1.txt","a") 

for i in range(1,4):
    name=input("Enter Subject Name : " )
    f.write("\n "+name)

f.close()