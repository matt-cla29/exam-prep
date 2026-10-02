import pandas as pd

df = pd.read_csv('data2.csv', sep=r'\s+')
 
new_df = df.dropna()
 
print(new_df.to_string())
 
