import json

with open("myjson.json","r") as f:
    data=json.load(f)
    print(data)