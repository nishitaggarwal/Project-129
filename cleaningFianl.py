
import pandas as pd
import csv

df = pd.read_csv('Dwarf_Planets_data.csv')

df = df[df["Radius"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Distance"].notna()]



df.to_csv('final_data.csv')

