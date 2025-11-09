# keyword argument means at time passing value also write its key name

# idf you want to pass the only keyword argum ent use """"[*,]"""" that not alow positional argument

def main(*,name="Yogesh"):
        print(name)

main(name="ram")# ist only allow key and value pair
main()
# main("ram")# its raise error


