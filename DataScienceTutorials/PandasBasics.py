import pandas as pd

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
#print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
#print(brics['population'])

arbeiter = pd.read_csv('Data Science Tutorials/bspcsvdatei.csv')
#print(arbeiter)

arbeiter = pd.read_csv('Data Science Tutorials/bspcsvdatei.csv', index_col= 0)
#print(arbeiter['Name'])
#print(arbeiter[['Name']])
print(arbeiter[['Name', 'Alter']])
print(arbeiter[0:4])
print(arbeiter.iloc[2])
print(brics.loc[['BR','RU']])
