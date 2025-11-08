score=1

def update():
    global score
    score+=10

    print("Inside The  Function= ",score)


# score+=10
update()
print("Outside The Function : ",score)