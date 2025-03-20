# #1
# from string import *
# vokaali=["a", "e", "o", "i", "ü", "õ", "ä"]
# konsontanti="qwrtpsdfghklzxcvbnm"
# numbrid=digits
# märkid=punctuation
# v=k=n=m=t=0
# tekst=input("Sisend (sõna või lause): ").lower()
# tekst_list=list(tekst)
# if tekst_list.index(" ")>0:
#     print("See on lause")
#     for s in tekst_list:
#         if s in vokaali:
#             v+=1
#         elif s in konsontanti:
#             k+=1
#         elif s in numbrid:
#             n+=1
#         elif s in märkid:
#             m+=1
#         elif s==" ":
#             t+=1
#     print(f"V: {v}\nK: {k}\nN: {n}\nM: {m} \nT: {t}")
# else:
#     print(f"kokku on {len(tekst_list)}")
    
#2
n = int(input("Введите количество элементов: "))
elements = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]
m = int(input("Введите количество элементов, которые нужно поменять местами: "))
for i in range(m // 2):
    elements[i], elements[m - 1 - i] = elements[m - 1 - i], elements[i]
print("Изменённый список:", elements)
