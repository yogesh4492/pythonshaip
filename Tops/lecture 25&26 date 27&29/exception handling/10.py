class validatorException(Exception):
    pass

try:
    username=input("ENter Username : ")
    password=input("Enter Password: ")
    if len(username)>4:
        if len(password)>8:
            print("valid user")
        else:
            raise validatorException("PAssword length must be 8  or more than 8 character ")
    else:
        raise validatorException("username must be more than 4 character")
    
except validatorException as e:
    print("error message",e)