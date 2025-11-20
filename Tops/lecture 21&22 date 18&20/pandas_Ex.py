import pandas as pd

"""
1)Series: which is similiar likje list whiich represent 1d array
           which is represent single row based record of table
2)DataFrame : which is similiar like 2D array

"""

import pandas as pd

products=pd.Series([45,84,57,78,99],index=['mobile','tv','laptop','fridge','Ac'])


print(products)
print(products['mobile'])