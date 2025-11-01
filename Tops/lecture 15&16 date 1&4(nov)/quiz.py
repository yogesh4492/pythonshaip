# nested dictionary

Quiz={
    1:{
        'que':'which is most powerfiull programming language ?',
        "ans":'python'
    },
    2:{
        'que':'which is use for base programming language ?',
        "ans":'c'
    },
    3:{
        'que':'which team won 2024 worldcup?',
        "ans":'india'
    }
}


for i in range(1,len(Quiz)+1):
    print(f" Que ({i}) . {Quiz[i].get('que')}")
    user_ans=input("Enter Answer =").lower()

    if user_ans==Quiz[i].get('ans').lower():
        print("right")
    else:
        print("Wrong")

# for i in Quiz:
#     print(f" Que ({i}) . {i['que']}")
#     user_ans=input("Enter Answer =").lower()

#     if user_ans==i['ans'].lower():
#         print("right")
#     else:
#         print("Wrong")

