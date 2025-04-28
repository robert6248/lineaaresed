from random import *  # Импортируем функцию случайного выбора

# Функция, чтобы считать данные из файла и сохранить в словарь
def loe_andmed(failinimi):
    sõnastik = {}  # Создаем пустой словарь
    try:
        with open(failinimi, 'r', encoding='utf-8-sig') as f:
            for rida in f:
                riik, pealinn = rida.strip().split('-')  # Разделяем строку по символу '-'
                sõnastik[riik] = pealinn  # Добавляем в словарь: ключ - страна, значение - столица
    except FileNotFoundError:
        print("Faili ei leitud.")
    return sõnastik

# Функция для поиска страны или столицы
def otsi(sõnastik):
    otsing = input("Sisesta riik või pealinn: ").strip()
    if otsing in sõnastik:
        print(f"{otsing} pealinn on {sõnastik[otsing]}")
    elif otsing in sõnastik.values():
        for riik in sõnastik:
            if sõnastik[riik] == otsing:
                print(f"{otsing} on riigi {riik} pealinn")
                break
    else:
        print("Ei leitud.")
        lisa = input("Kas soovid selle lisada? (jah/ei): ").strip().lower()
        if lisa == "jah":
            riik = input("Sisesta riik: ")
            pealinn = input("Sisesta pealinn: ")
            sõnastik[riik] = pealinn
            print("Lisatud!")

# Функция для исправления ошибки
def paranda(sõnastik):
    nimi = input("Sisesta riik või pealinn, mida soovid parandada: ").strip()
    if nimi in sõnastik:
        uus_pealinn = input("Sisesta uus pealinn: ")
        sõnastik[nimi] = uus_pealinn
        print("Pealinn uuendatud!")
    elif nimi in sõnastik.values():
        for riik in sõnastik:
            if sõnastik[riik] == nimi:
                uus_riik = input("Sisesta uus riik: ")
                sõnastik[uus_riik] = nimi
                del sõnastik[riik]
                print("Riik uuendatud!")
                break
    else:
        print("Andmeid ei leitud.")

# Функция для проверки знаний
def testi(sõnastik):
    õiged = 0  # Количество правильных ответов
    kogus = int(input("Mitu küsimust soovid? "))  # Сколько вопросов
    paarid = list(sõnastik.items())  # Преобразуем словарь в список пар (страна, столица)

    for _ in range(kogus):
        riik, pealinn = choice(paarid)  # Выбираем случайную пару
        if choice([True, False]):  # Случайно решаем, что спрашивать
            vastus = input(f"Mis on riigi {riik} pealinn? ")
            if vastus.strip().lower() == pealinn.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus: {pealinn}")
        else:
            vastus = input(f"Millise riigi pealinn on {pealinn}? ")
            if vastus.strip().lower() == riik.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus: {riik}")

    protsent = round((õiged / kogus) * 100)
    print(f"Sinu tulemus: {õiged}/{kogus} ({protsent}%)")

# Главная программа
sõnastik = loe_andmed("riigid_pealinnad.txt")  # Загружаем словарь из файла

# Цикл выбора действий
while True:
    print("\nValikud:")
    print("1 - Otsi riiki või pealinna")
    print("2 - Paranda andmeid")
    print("3 - Testi oma teadmisi")
    print("4 - Välju programmist")
    valik = input("Sisesta number: ")

    if valik == "1":
        otsi(sõnastik)
    elif valik == "2":
        paranda(sõnastik)
    elif valik == "3":
        testi(sõnastik)
    elif valik == "4":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik. Proovi uuesti.")
