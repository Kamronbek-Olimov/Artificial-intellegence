import pandas as pd
df = pd.DataFrame ({'ism':['Kamronbek','Samandar','Diyorbek','Shuxrat', 'Farrux','Oybek','Shoyat','Sayyodbek','Xurshid','Ibrohim'],
                    'Familya':['Samiyev','Tursunov','Samigjonov','Toirov','Salimov','Akramov','Maqsudov','Toirov','Odilov','Burxonov'],
                    'Yoshi':['19','19','19','19','19','19','19','20','19','19'],
                    'Kursi':['2','2','2','2','2','2','2','2','2','2']
                    })
print (df)
df.to_excel('631guruh.xlsx', index=False, sheet_name='Sheet1')