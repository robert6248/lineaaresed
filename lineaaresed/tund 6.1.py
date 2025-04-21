import random


sonastik = dict([
    ('koer', 'собака'),
    ('kass', 'кошка'),
    ('maja', 'дом'),
    ('auto', 'машина'),
    ('päike', 'солнце')
])


def tolgi_est_rus(sona):
    return sonastik.get(sona, "See sõna pole sõnastikus!")

def tolgi_rus_est(sona):
    return next((est for est, rus in sonastik.items() if rus == sona), "Это слово не найдено в словаре!")

def lisa_sona():
    sonastik[input("Sisesta uus sõna eesti keeles: ")] = input("Sisesta vene tõlge: ")
    print("Sõna lisatud!")

def paranda_sona():
    vana_sona = input("Sisesta sõna, mida soovid parandada: ")
    if vana_sona in sonastik:
        sonastik[vana_sona] = input("Sisesta новый vene tõlge: ")
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud!")

def testi_teadmisi():
    for est in random.sample(list(sonastik.keys()), 3):
        if input(f"Sisesta vene tõlge sõnale '{est}': ") == tolgi_est_rus(est):
            print("Õige!")
        else:
            print(f"Vale! Õige vastus on: {tolgi_est_rus(est)}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def main():
    while True:
        print("\n1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")
        valik = input("Tee oma valik: ")

        if valik == '1':
            print(f"Tõlge vene keelde: {tolgi_est_rus(input('Sisesta sõna eesti keeles: '))}")
        elif valik == '2':
            print(f"Tõlge eesti keelde: {tolgi_rus_est(input('Sisesta sõna vene keeles: '))}")
        elif valik == '3':
            lisa_sona()
        elif valik == '4':
            paranda_sona()
        elif valik == '5':
            testi_teadmisi() 
        elif valik == '6':
            print("Kena päeva!")
            break
        else:
            print("Vale valik, proovi uuesti!")
main()
