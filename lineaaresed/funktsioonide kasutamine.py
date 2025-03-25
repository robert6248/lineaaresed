from kasutaja_funktsioonide import *

a=float(input("Arv1:"))
b=float(input("Arv2:"))
t=input("Tehe:")
vastus=arithmetic(a,b,t)
print(vastus)

vastus=arithmetic(float(input("Arv1:")),float(input("Arv2:")),input("Tehe:"))
print(vastus)

#is_year_leap funktsiooni kasutamine
aasta=int(input("Mis aasta tahad kontrolliida?? "))
if aasta>:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigasta")
