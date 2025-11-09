#in this program mixed argument allowed in function 
# one thing that notice positional argument also placed before the keyword argument

def main(name="Yogesh",/,*,roll=101,score=99):# here name is positional argument and rolland score is keyword argument
       print(name,roll,score)
    
main("ram",score=89,roll=102)
main()

