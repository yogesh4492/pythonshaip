f=open("myfile.txt","r")


data=f.readlines() # it will fetch all lines and convert into list format

print(data)
print(f"no of lines in file :{len(data)}")