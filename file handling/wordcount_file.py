""" Count total words from the file """


with open("myfile.txt","r") as f:
    data=f.read()
    words=data.split()
    print("length of words in ,list : ",len(words))
    print(words)