"""
Dataframe : Dataframe is similiar like full table row and column


"""

import pandas as pd

data={
    "customer":['yogesh','yash','ram','rahul','rohit'],
    "product":['mobile','bike','tv','laptop','car'],
    "price":[10000,100000,20000,30000,5600000]

}

df=pd.DataFrame(data)

print(df)