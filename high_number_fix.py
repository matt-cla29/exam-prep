import pandas as pd

df = pd.read_csv('data3.csv', sep=r'\s+')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

df.loc[7, 'Duration'] = 45

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())