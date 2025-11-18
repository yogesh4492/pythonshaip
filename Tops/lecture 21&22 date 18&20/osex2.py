import os

if os.path.exists("Myfolder"):
    os.rmdir("Myfolder")
else:
    print("Folder Does Not exists")