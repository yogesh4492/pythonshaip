"""
Json : java script object notation

 json is a combin ation off json array and json object


 {
   "key": value
 }

"""

import json

data={
    'subject':"python",
    "score": 89
}

with open("myjson.json","w") as f:
    json.dump(data,f,indent=4)


print("file creted succeffully!!")