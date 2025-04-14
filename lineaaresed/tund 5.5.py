import random

#8
def patsiendid():
    nimed = []
    vitamiinid = []
    n = int(input("Patsientide arv: "))
    for i in range(n):
        nimi = input("Nimi: ")
        vit = random.randint(10, 100)
        nimed.append(nimi)
        vitamiinid.append(vit)
    while True:
        print("""
1. Alla 30 tase
2. Keskmine tase
3. K parimat
4. Otsi nime järgi
5. Välju
""")
        v = input("Valik: ")
        if v == "1":
            for nimi, vit in zip(nimed, vitamiinid):
                if vit < 30:
                    print(nimi, vit)
        elif v == "2":
            print("Keskmine:", sum(vitamiinid) / len(vitamiinid))
        elif v == "3":
            k = int(input("Mitu parimat? "))
            for nimi, vit in sorted(zip(nimed, vitamiinid), key=lambda x: x[1], reverse=True)[:k]:
                print(nimi, vit)
        elif v == "4":
            otsing = input("Nimi: ")
            for nimi, vit in zip(nimed, vitamiinid):
                if otsing.lower() in nimi.lower():
                    print(nimi, vit)
        elif v == "5":
            break

patsiendid()
