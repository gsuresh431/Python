import pandas as pd 
import numpy as np 
'''
df = pd.DataFrame(dict)
df.to_csv("file.csv")
'''

dict1 = {
    'name': ['Soumya', 'Suresh', 'Shreyansh', 'Ashok'],
    'marks': [99, 100, 98, 97],
    'city': ['bbsr', 'hyd', 'Bihar', 'secdbad']
}

df = pd.DataFrame(dict1)
df.to_csv("sample.csv", index=False)
print(df)         
print(df.head(2)) # print first two indexes (index=row)
print(df.tail(2)) # print last two indexes
print(df.describe()) # gives mathematical stats related to numerical columns of df
print(df['name']) # prints the name column
df.index = ['first', 'second', 'third', 'fourth'] # Giving each index(aka row) a specific name
print(df)         
df['name'][1] = 'Suresh Gorella' # Modifying the value
print(df)
print(df.to_csv("output.csv"))