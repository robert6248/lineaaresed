#1
# def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
#     """Funktsioon töötab nagu lihtne kalkuaator
#     + - liitmine
#     - - lahutamine
#     * - korrutamine
#     / - jagamine
#     Kui sisend ei ole järjendus[+,-,/,*],siis tagastab sõne "Tundmatu tehe"
#     :param float arv1: Sisend ujukomaarvi tüübina
#     :param float arv2: Sisend ujukomaarvi tüübina
#     :param str tehe: Sisend listist [+,-,/,*]
#     :rtype: varMääramata tüüp (float või str)
#     """
#     if tehe  in ["+","-","*","/"]:
#         if arv2==0 and tehe=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(arv1)+tehe+str(arv2))
#     else:
#         vastus="Tundmatu teha"
#     return vastus

#2
# def is_year_leap(aasta:int)->bool:
#     """Liigaasta leidmine
#     Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
#     :param int aasta:Sisend kasutajalt
#     :rtype bool tõeväärsuses formaadis tulemuus
#     """
#     if aasta%4==0:
#         v=True
#     else:
#         v=False
#         return v

#3
# def square(külg:float)->any:
#     """
#     Funktsioon tagastab ruudu ümbermõõt, ruudu pindala ja ruuudu diagonaal
#     """
#     S=külg**2
#     P=4*külg
#     d=(2)**(1/2)*külg
#     return S,P,d

#4
# def season(param: int) -> str:
#     """
#     Funktsioon, mis võtab vastu kuu numbri ja tagastab vastava aastaaja nimetuse.
#     :param param: Kuu number (1-12)
#     :rtype: String, mis sisaldab aastaaja nimetust (talv, kevad, suvi, sügis)
#     """
#     if param in [1, 2, 12]:
#         H = "Talv"  
#     elif param in [3, 4, 5]:
#         H = "Kevad"  
#     elif param in [6, 7, 8]:
#         H = "Suvi"  
#     elif param in [9, 10, 11]:
#         H = "Sügis"  
#     else:
#         H = "Vale kuu" 
#     return H

#5
# def bank(summa: float, aastad: int)->float:
#     """
#     Funktsioon arvutab kasutaja pangakontol oleva summa koos intressidega.
#     :param summa: algne sissemakse summa
#     :param aastad: aastate arv
#     :return: lõppsumma pärast kõiki intresse
#     """
#     for aasta in range(aastad):
#         summa*=1.1
#     return summa

from random import *
# #6
# def is_prime(a=randint(1,10000))->bool:
#     """
#     Funktsioon, mis kontrollib, kas number on algarv.
#     :param a: Arv, mille kohta kontrollitakse, kas see on algarv (0 kuni 1000)
#     :return: True, kui number on algarv, vastasel juhul False
#     """
#     print(a)
#     v=True
#     for jagaja in range(2,a):
#         if a%jagaja==0: 
#             v=False
#     return v

#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    """
    if päev in range(1,32) and kuu in [1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v