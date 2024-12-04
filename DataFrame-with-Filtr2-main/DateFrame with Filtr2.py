import pandas as pd
df = pd.read_excel("titanik.xlsx")
print(data.head())
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
filtr = df[df['Age'] <15]
print(filtr)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
filtr = df[df['Age'] >15]
print(filtr)