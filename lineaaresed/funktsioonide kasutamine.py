from kasutaja_funktsioonide import *
from math import *
# a=float(input("Arv1:"))
# b=float(input("Arv2:"))
# t=input("Tehe:")
# vastus=arithmetic(a,b,t)
# print(vastus)

# vastus=arithmetic(float(input("Arv1:")),float(input("Arv2:")),input("Tehe:"))
# print(vastus)

# #is_year_leap funktsiooni kasutamine
# aasta=int(input("Mis aasta tahad kontrolliida?? "))
# if aasta>0:
#     v=is_year_leap(aasta)
#     print(v)
#     if v:
#         print(f"{aasta} on liigaasta")
#     else:
#         print(f"{aasta} ei ole liigasta")

#square() kasutamine:
#kontroll while True ja try except
# while True:
#     try:
#         a = float(input("Ruudu külg= "))
#         if a <= 0:
#             print("Сторона квадрата должна быть положительным числом. Попробуйте снова.")
#             continue
#         perimeter, pindala, diagonal = square(a)
#         print(f"Ruudu perimeeter: {perimeter}")
#         print(f"Ruudu pindala: {area}")
#         print(f"Ruudu diagonaal: {diagonal}")
#         break
#     except:
#         print("Viga! Palun sisestage arvu väärtus ruudu külje jaoks.")

#season
# while True:
#     try:
#         month = int(input("Sisesta kuu number (1-12): "))
#         if 1 <= month <= 12:
#             print(f"See kuu kuulub: {season(month)}") 
#         else:
#             print("Palun sisesta kuu number vahemikus 1-12.")  
#     except:
#         print("Viga! Palun sisesta number.") 
 

# #bank
# while True:
#     try: 
#         summa = float(input("Sisesta algne summa (eurodes): "))
#         aastad = int(input("Sisesta aastate arv: "))
#         if summa <= 0 or aastad <= 0:
#             print("Summa ja aastad peavad olema positiivsed arvud. Proovige uuesti.")
#         final_sum = bank(summa, aastad)
#         print(f"Summa {aastad} aasta pärast: {final_sum} eurot.")
#     except:
#         print("Viga! Palun sisestage korrektne number.")

#numbrid
# while True:
#     try:
#         number = int(input("Sisesta number, et kontrollida, kas see on algarv (0-1000): "
#         if 0 <= number <= 1000:
#             print(f"Kas {number} on algarv? {is_prime(number)}")
#         else:
#             print("Palun sisesta number vahemikus 0 kuni 1000.")
#     except ValueError:
#         print("Viga! Palun sisestage korrektne number.")
# random_number = randint(0, 1000)