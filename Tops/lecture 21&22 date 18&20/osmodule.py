import os

if os.path.exists("Myfolder"):
    print("folder already exists")
else:
    os.mkdir("Myfolder")
    print("folder created")