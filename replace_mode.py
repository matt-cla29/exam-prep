import pandas as pd

df = pd.read_csv('data2.csv', sep=r'\s+')

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())