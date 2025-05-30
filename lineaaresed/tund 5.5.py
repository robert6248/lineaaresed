import random
from patients import create_patients, patients_below_30, average_vitamin_level, top_k_patients, search_patient

n = int(input("Sisesta patsientide arv: "))

nimed, vitamiinid = create_patients(n)

while True: 
    print("""
    1. Patsientide vitamiinitase alla 30
    2. Keskmine vitamiinitase
    3. K parimat patsienti
    4. Patsientide otsing nime järgi
    5. Kõik patsiendid
    6. Väljumine
    """)

    valik = input("Vali menüüpunkt: ")

    if valik == "1": 
        result = patients_below_30(n, nimed, vitamiinid)
        if result:
            for name, vit in result:
                print(name, vit)
        else:
            print("Puuduvad patsiendid, kelle vitamiinitase on alla 30.")

    elif valik == "2":
        keskmine = average_vitamin_level(vitamiinid)
        print("Keskmine vitamiinitase:", keskmine)

    elif valik == "3":
        try:
            k = int(input("Sisesta parimate patsientide arv: "))
            if k > n:
                print("Parimate patsientide arv ei saa olla suurem kui patsientide koguarv.")
            else:
                result = top_k_patients(k, nimed, vitamiinid)
                for name, vit in result:
                    print(name, vit)
        except:
            print("Palun sisesta korrektne number.")

    elif valik == "4":
        otsing = input("Sisesta patsiendi nimi otsinguks: ")
        result = search_patient(otsing, nimed, vitamiinid)
        if result:
            for name, vit in result:
                print(name, vit)
        else:
            print("Patsienti ei leitud.")

    elif valik == "5":
        print("Kõik patsiendid:")
        for name, vit in zip(nimed, vitamiinid):
            print(name, vit)

    elif valik == "6":
        print("Programmist väljumine.")
        break
