Quiz={
    '1':{
        "Que":"which Team Won 2025 Women World Cup ?",
        "Ans":"India"
    },
    "2":{
        "Que":"which language is developed by denis richie in 1972? ",
        "Ans":"C Language"
        
    },
    "3":{
        "Que":"Python Programming Language Developed By ?",
        "Ans":"Guido VAn Rossum"
    }
}

for i in Quiz:
    print(Quiz[i].get('Que'))
    user_ans=input("ENter Answer = ")
    if user_ans.lower()==Quiz[i].get('Ans').lower():
        print("Right Answer !")
    else:
        print("Wrong Answer!")
    
