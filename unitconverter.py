import pandas as pd
import csv

df = pd.read_csv('final_data.csv')

df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1,inplace=True)
print(df.head())
df = df.dropna()

df["Radius"] = 0.102763*df["Radius"]


df["Mass"] = 0.000954588*df["Mass"]



df.reset_index(drop=True,inplace=True)
df.to_csv("unit_converted_stars.csv")
