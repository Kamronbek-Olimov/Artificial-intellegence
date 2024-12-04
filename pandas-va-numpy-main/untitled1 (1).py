import pandas as pd
data = {
    'Ism': ['Ali', 'Vali', 'Sardor'],
    'Yoshi': [25, 28, 30] 
}
df = pd.DataFrame(data)

# 2. Ma'lumotlarni ko'rish
print(df)

# 3. Filtrlash
young_people = df[df['Yoshi'] < 30]
print("30 yoshdan kichiklar:\n", young_people)

df['Yoshi'] += 1 
print("Yangilangan DataFrame:\n", df)

# 5. CSV formatda saqlash
df.to_csv('data.csv', index=False)