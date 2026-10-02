import pandas as pd

df = pd.read_csv('data2.csv')

df.dropna(inplace = True)

print(df.to_string())
