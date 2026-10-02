import pandas as pd

df = pd.read_csv('data4.csv')

print(df.duplicated())