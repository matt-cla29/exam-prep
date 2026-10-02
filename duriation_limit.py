import pandas as pd

df = pd.read_csv('data3.csv', sep=r'\s+')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())