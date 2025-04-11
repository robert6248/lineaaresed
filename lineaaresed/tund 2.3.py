#from curses.ascii import isalpha



print("Tere! Olen sinu uus sõber - Python!")

nimi = input("Sisesta oma nimi: ")
if nimi.isalpha()!=True:
    print("Sisesta nimi, ei ole numbrid")
print(f"{nimi}, oi kui ilus nimi!")

try:
    valik = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if valik == 1:
        pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
        mass = float(input("Sisesta oma kehakaal kilogrammides: "))
        
        if pikkus > 0 and mass > 0:
            kmi = mass / ((pikkus / 100) ** 2)
            print(f"{nimi}! Sinu keha indeks on: {kmi}")
            
            if kmi < 16:
                hinnang = "Tervisele ohtlik alakaal"
            elif kmi < 20:
                hinnang = "Alakaal"
            elif kmi < 26:
                hinnang = "Normaalkaal"
            elif kmi < 31:
                hinnang = "Ülekaal"
            elif kmi < 36:
                hinnang = "Rasvumine"
            elif kmi < 41:
                hinnang = "Tugev rasvumine"
            else:
                hinnang = "Tervisele ohtlik rasvumine"
            
            print(f"{nimi}, Sinu KMI hinnang on: {hinnang}")
        else: 
            print("Viga! Pikkus ja kaal peavad olema positiivsed arvud.")
    elif valik == 0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vigane valik! Palun sisesta 0 või 1.")
except:
    print("Viga! Palun sisesta ainult numbrid.")

print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")