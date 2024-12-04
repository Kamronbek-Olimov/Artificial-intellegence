import pandas as pd
df = pd.DataFrame ({'ism':['Muhammadaziz','Nurmuhammad','Merojiddin','Shuxrat', 'Shohrux','Oybek','Shoyat','Mohichexra','Xurshid','Ibrohim'],
                    'Familya':['Rozaliyev','Jumanazarov','Bahtiyorjonov','Shamsiddinov','Salimov','Akramov','Maqsudov','Yusupaliyeva','Odilov','Burxonov'],
                    'Yoshi':['19','19','19','19','19','19','19','20','19','19'],
                    'Kursi':['2','2','2','2','2','2','2','2','2','2']
                    })
print (df)
df.to_excel('631guruh.xlsx', index=False, sheet_name='Sheet1')