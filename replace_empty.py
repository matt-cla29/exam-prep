import pandas as pd

df = pd.read_csv('data2.csv', sep=r'\s+')

df = df.astype(str)
df.fillna('130', inplace=True)

print(df.to_string())
