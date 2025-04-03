import pandas as pd


df_conjunto = pd.read_csv('03 shopping_trends.csv')
print(df_conjunto.info())
print(df_conjunto.head())
print(df_conjunto.describe())
print(df_conjunto.tail())
print(df_conjunto.columns)
print(df_conjunto['Customer ID'].describe())
print(df_conjunto['Customer ID'].unique())
