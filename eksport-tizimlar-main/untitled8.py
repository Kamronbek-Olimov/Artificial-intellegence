def kasallik_tashxisi(belgi):
    if belgi == "istima":
        return "Parasetamol iching"
    elif belgi == "tish og'rig'i":
        return "Qupen iching"
    elif belgi == "qorin og'rig'i":
        return "Levomitsin"
    elif belgi == "bosh og'rig'i":
        return "Ibuprofen iching"
    elif belgi == "gripp":
        return "Tamiflu iching"
    elif belgi == "allergiya":
        return "Antihistamin iching"
    elif belgi == "yurak og'rig'i":
        return "Nitroglycerin oling"
    elif belgi == "qon ketishi":
        return "Dabigatran qabul qiling"
    elif belgi == "asqotish":
        return "Cetrizine iching"
    elif belgi == "qon bosimi yuqoriligi":
        return "Anaprilin iching"
    else:
        return "Shifokorga murojaat qiling"
belgi = input("Kasallik belgisini kiriting: ")
natija = kasallik_tashxisi(belgi)
print(natija)

def kitob_tavsiyasi(tur):
    if tur == "fantastika":
        return "Jules Verne'ning 'Yer markaziga sayohat' kitobini o'qing"
    elif tur == "tarixiy":
        return "Walter Isaacson'ning 'Leonardo da Vinci' asarini o'qing"
    elif tur == "sarguzasht":
        return "Mark Twain'ning 'Tom Sawyerning sarguzashtlari' kitobini o'qing"
    elif tur == "ilmiy":
        return "Stephen Hawking'ning 'Zamonga qisqa nazar' kitobini o'qing"
    elif tur == "psixologiya":
        return "Daniel Kahneman'ning 'Thinking, Fast and Slow' kitobini o'qing"
    elif tur == "biografiya":
        return "Michelle Obama'ning 'Becoming' kitobini o'qing"
    elif tur == "detektiv":
        return "Agatha Christie'ning 'Murder on the Orient Express' kitobini o'qing"
    elif tur == "romantik":
        return "Jane Austen'ning 'Pride and Prejudice' kitobini o'qing"
    elif tur == "motivatsiya":
        return "Robin Sharma'ning 'The Monk Who Sold His Ferrari' kitobini o'qing"
    elif tur == "falsafa":
        return "Platon'ning 'Respublika' asarini o'qing"
    else:
        return "Bu turdagi kitob uchun shifokorga emas, kutubxonaga murojaat qiling :)"
tur = input("Kitob turini kiriting: ")
natija = kitob_tavsiyasi(tur)
print(natija)