# keyword arguments

# main benifit is that no need to check order of function parameter js=ust pass argument by assinging value

def main(name="ram",roll=102):# alswo gived some default
    print(name,roll)

main(roll=101,name="Yogesh") # order does not mater
main() #uits print default data
# 

#positional and keyword argument mixed up
def main(name,roll,score):# always positional argument t first or beforr keyword argument
    print(name,roll,score)

main("yogesh",score=99,roll=101)




