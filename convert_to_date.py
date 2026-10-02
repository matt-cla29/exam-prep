import pandas as pd

df = pd.read_csv('data3.csv', sep=r'\s+')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())