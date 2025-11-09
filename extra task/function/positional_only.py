# positional means those argument which take value as given order
# if you want ony [posional argumeent [pass to function]] """ [use ',/'] """ that not allow keyword argument

def main(name="Yogesh",/):# this cannot alow keyword argument
    print("name= ",name)

main("ram")
main()
# main(name="yog")# its raise error 

