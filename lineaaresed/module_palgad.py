p = []
i = []

def lisa():
    nimi = input("Nimi: ")
    if nimi.isalpha():
        try:
            palk = float(input("Palk: "))
            i.append(nimi)
            p.append(palk)
            print("Lisatud!")
        except:
            print("Palk peab olema number!")


def kustuta():
    nimi = input("Kustuta nimi: ")
    while nimi in i:
        ind = i.index(nimi)
        i.pop(ind)
        p.pop(ind)
    print("Kustutatud!")


def suurim():
    if p:
        m = max(p)
        for j in range(len(p)):
            if p[j] == m:
                print(f"{i[j]} saab suurimat palka: {m}")


def vaiksem():
    if p:
        m = min(p)
        for j in range(len(p)):
            if p[j] == m:
                print(f"{i[j]} saab vaiksemat palka: {m}")


def kasvav():
    for x in range(len(p)):
        for y in range(x + 1, len(p)):
            if p[x] > p[y]:
                p[x], p[y] = p[y], p[x]
                i[x], i[y] = i[y], i[x]


def kahanev():
    for x in range(len(p)):
        for y in range(x + 1, len(p)):
            if p[x] < p[y]:
                p[x], p[y] = p[y], p[x]
                i[x], i[y] = i[y], i[x]

def otsi():
    nimi = input("Nimi: ")
    for j in range(len(i)):
        if i[j] == nimi:
            print(f"{nimi} palk: {p[j]}")
            return
    print("Ei leitud")

def filtr():
    try:
        s = float(input("Summa: "))
        v = input("Rohkem kui? (jah/ei): ")
        for j in range(len(p)):
            if (v == "jah" and p[j] > s) or (v != "jah" and p[j] < s):
                print(f"{i[j]}: {p[j]}")
    except:
        print("Viga!")
