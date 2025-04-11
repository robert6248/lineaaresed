
p=[]
i=[]
def Lisa_andmed(p:list,i:list):
    """
   Добавляем несколько людей и зарплат
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                    print("Palk on arv!")
                break
                print("Andmed on lisatud!")
                p.append(palk)
                i.append(nimi)
        except:
            print("Kirjuta ainult tähtede kasutades!")

        
def Kustuta_andmed(p:list,i:list):
    """ 
    Удалить человека и его зарплату
    """
    try:
        nimi=input("Nimi: ")
        if nimi.isalpha():
            k=i.count(nimi)
            if k>0:
                for j in range(k):
                    ind=i.index(nimi)
                    i.pop(ind)
                    p.pop(ind)
                print("Andmed on kustutatud!")
            else:
                print("Andmed on puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades!")

def Suurim_palk(p:list,i:list):
    """ 
    Самая большая зарплата и кто ее получает
    """
    max_palk=max(p)
    print(f"Suurim palk on {max_palk}")
    k=p.count(max_palk)
    ind=p.index(max_palk)
    for j in range(k):
        ind=p.index(max_palk,ind)
        print(f"Suurim palk on {max_palk} ja selle saab {i[ind]}")
        ind=ind+1

def Väiksem_palk(p:list,i:list):
    """ 
    Самая маленькая зарплата и кто ее получает
    """
    min_palk=min(p)
    print(f"Väiksem palk on {min_palk}")
    k=p.count(min_palk)
    ind=p.index(min_palk)
    for j in range(k):
        ind=p.index(min_palk,ind)
        print(f"Väiksem palk on {min_palk} ja selle saab {i[ind]}")
        ind=ind+1

def sorteerimine_kasvav(p:list,i:list)->any:
    """ 
    Упорядочить зарплаты в порядке возрастания вместе с именами
    :param p: Список зарплат
    :type p: list
    :param i: Список имён
    :type i: list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def sorteerimine_kahanev(p:list,i:list)->any:
    """ 
    Упорядочить зарплаты в порядке убывания вместе с именами
    :param p: Список зарплат
    :type p: list
    :param i: Список имён
    :type i: list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]<p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def Võrdsed_palgad(p:list,i:list):
    """
   Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def palgaotsing(p:list,i:list):
    """
    Сделать поиск зарплаты по имени человека. 
    """
    nimi=input("Sisesta nimi otsinguks: ")
    leitud=False
    for j in range(len(i)): #проходим по всем индексам
        if i[j]==nimi: #если имя совпадает 
            print(f"{i[j]} saab palka {p[j]}") # написать имя человека и какую зарплату он получает
            leitud=True
        if leitud==False:
            print(f"({nimi} kohta andmeid ei leitud")

def filtr_palgad(p: list, i: list) -> None:
    """Вывести список людей, у которых зарплата больше или меньше заданной пользователем суммы.
    """
    try:
        summa = float(input("Sisesta summa, mille järgi filtreerida: "))  # Получаем сумму
        valik = input("Kas otsida inimesi, kelle palk on rohkem kui määratud summa? (jah/ei): ").strip().lower()  # Определяем, искать ли зарплаты больше или меньше
        if valik=="jah":
            rohkem=True
        else:
            rohkem=False
        valitud_inimesed = [(i[j], p[j]) for j in range(len(p)) if (rohkem and p[j] > summa) or (not rohkem and p[j] < summa)] # Фильтрация индексов с зарплатами больше или меньше указанной суммы
        if valitud_inimesed:  # Выводим результаты
            print(f"Inimesed, kelle palk on {'rohkem' if rohkem else 'vähem'} kui {summa}:")
            for nimi, palk in valitud_inimesed:
                print(f"{nimi}: {palk}")
        else:
            print("Ei leidnud inimesi, kes vastaksid kriteeriumitele.")
    except:
        print("Palun sisestage korrektne number!")

def Bonus_salary(p: list,i: list):
    """
    Своя функция по выбору. Добавляет прибавку к зарплате выбранному работнику, позволяя выбрать процент на какой зарплата увеличится
    """
    for idx, (name, salary) in enumerate(zip(i, p), 1):
        print("\nCurrent employees and salaries:")
        print(f"{idx}. {name}: {salary}$")
    try:
        choice = int(input("Valige töötaja: "))
        bonus= float(input("Kirjutage mittu protsentis palk tõuseb:"))
        if 0 <= choice < len(i) and bonus > 0:
            original_salary = p[choice]
            bonus_to = bonus / 100
            bonus_salary = original_salary * bonus_to + original_salary
            print(f"New salary is: {bonus_salary}$")
        else:
            print("Valge eksisteeriv töötaja ja valige bonus rohkem kui 0")
    except:
        print("Viga!")