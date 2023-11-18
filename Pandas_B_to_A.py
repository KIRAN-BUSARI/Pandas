import pandas as pd

df = pd.read_csv('services.csv') # Filename

print(df.head()) # This will print the top 5 list from a dataset

print(df.tail()) # This will print the Last 5 list from a dataset

print(df.columns) # To print all the columns name i.e index names

print(list(df.columns)) # To get the above output in the form of a list.

# dtype is used to know the datatype of any object