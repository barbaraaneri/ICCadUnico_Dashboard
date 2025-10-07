# Feito por Gustavo José da Silva Castro
# gustavocastro20042002@gmail.com

import csv
import pandas as pd

#Read CSV file into DataFrame
df = pd.read_csv('../BasesDeDados/PolisPCDaS.csv')

# Convert 'COD_IBGE' column to string
df['COD_IBGE'] = df['COD_IBGE'].astype(str)

# Filter rows where 'COD_IBGE' starts with '35'
df = df[df['COD_IBGE'].str.startswith('35')]

df.to_csv('PolisPCDaSSP.csv')