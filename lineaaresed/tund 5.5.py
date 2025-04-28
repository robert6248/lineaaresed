import random
from patients import create_patients, patients_below_30, average_vitamin_level, top_k_patients, search_patient

n = int(input("Введите количество пациентов: "))

nimed, vitamiinid = create_patients(n)

while True:
    print("""
    1. Пациенты с уровнем витаминов меньше 30
    2. Средний уровень витаминов
    3. K лучших пациентов
    4. Поиск пациента по имени
    5. Выход
    """)

    valik = input("Выберите пункт меню: ")

    if valik == "1":
        result = patients_below_30(n, nimed, vitamiinid)
        if result:
            for name, vit in result:
                print(name, vit)
        else:
            print("Нет пациентов с уровнем витаминов меньше 30.")

    elif valik == "2":
        keskmine = average_vitamin_level(vitamiinid)
        print("Средний уровень витаминов:", keskmine)

    elif valik == "3":
        try:
            k = int(input("Введите количество лучших пациентов: "))
            if k > n:
                print("Количество лучших пациентов не может быть больше общего числа пациентов.")
            else:
                result = top_k_patients(k, nimed, vitamiinid)
                for name, vit in result:
                    print(name, vit)
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    elif valik == "4":

        otsing = input("Введите имя пациента для поиска: ")
        result = search_patient(otsing, nimed, vitamiinid)
        if result:
            for name, vit in result:
                print(name, vit)
        else:
            print("Пациент не найден.")

    elif valik == "5":
        print("Выход из программы.")
        break