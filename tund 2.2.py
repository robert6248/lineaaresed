from math import *
# #1
# try:
#     arv=input("Sisesta arv: ")
#     if arv.isnumeric()
#         arv=int(arv)
#         if arv>0:
#             if arv%2==0:
#                 print("Paaris arv")
#             else:
#                 print("Paaritu")
#         else:
#             print("Negatiivne arv")
# except:
#     print("Kirjuta numbreid")


# #2
# try:
#     nurk1=float(input("Esimene nurk"))
#     nurk2=float(input("Teine nurk"))
#     nurk3=float(input("Kolmas nurk"))
#     if nurk1>0 and nurk2>0 and nurk3>0:
#         print("Nurgad on positiivsed")
#         if nurk1+nurk2+nurk3==180:
#             print("See on kolmnurk")
#             if nurk1==nurk2 and nurk2==nurk3:
#                 print("V�rgk�lgne kolmnurk")
#             elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
#                 print("V�rdvaarne kolmnurk")
#             else:
#                 print("Erik�lgne kolmnurk")
#         else:
#             print("See ei ole kolmnurk")
#     else:
#         print("Negatiivsed nurgad ei soobi")
# except:
#     print("Sisesta ujukomaarvud")

# #3
# try:
#     soov = input("Kas sa tahad dekodeerida?").lower()
#     if soov == "jah":
#         try:
#             nr = int(input("P�eva number: "))
#             if nr in range(1, 8):
#                 if nr == 1:
#                     print("Esmasp�ev")
#                 elif nr == 2:
#                     print("Teisip�ev")
#                 elif nr == 3:
#                     print("Kolmap�ev")
#                 elif nr == 4:
#                     print("Neljap�ev")
#                 elif nr == 5:
#                     print("Reede")
#                 elif nr == 6:
#                     print("Laup�ev")
#                 elif nr == 7:
#                     print("P�hap�ev")  
#         except ValueError:
#             print("Palun sisesta number.")
# except:
#     print("Mul on vaja vastus Jah v�i Ei")


#4
p�ev = int(input("S�nnip�ev: "))
kuu = int(input("S�nnikuu: "))

if (kuu == 3 and p�ev >= 21) or (kuu == 4 and p�ev <= 19):
    m�rk = "J��r"
elif (kuu == 4 and p�ev >= 20) or (kuu == 5 and p�ev <= 20):
    m�rk = "S�nn"
elif (kuu == 5 and p�ev >= 21) or (kuu == 6 and p�ev <= 20):
    m�rk = "Kaksikud"
elif (kuu == 6 and p�ev >= 21) or (kuu == 7 and p�ev <= 22):
    m�rk = "V�hk"
elif (kuu == 7 and p�ev >= 23) or (kuu == 8 and p�ev <= 22):
    m�rk = "L�vi"
elif (kuu == 8 and p�ev >= 23) or (kuu == 9 and p�ev <= 22):
    m�rk = "Neitsi"
elif (kuu == 9 and p�ev >= 23) or (kuu == 10 and p�ev <= 22):
    m�rk = "Kaalud"
elif (kuu == 10 and p�ev >= 23) or (kuu == 11 and p�ev <= 21):
    m�rk = "Skorpion"
elif (kuu == 11 and p�ev >= 22) or (kuu == 12 and p�ev <= 21):
    m�rk = "Ambur"
elif (kuu == 12 and p�ev >= 22) or (kuu == 1 and p�ev <= 19):
    m�rk = "Kaljukits"
elif (kuu == 1 and p�ev >= 20) or (kuu == 2 and p�ev <= 18):
    m�rk = "Veevalaja"
elif (kuu == 2 and p�ev >= 19) or (kuu == 3 and p�ev <= 20):
    m�rk = "Kalad"
print(f"Sinu t�hem�rk on: {m�rk}")


#5

