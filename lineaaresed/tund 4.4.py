#1
from string import *
vokaali=["a", "e", "o", "i", "ü", "õ", "ä"]
konsontanti="qwrtpsdfghklzxcvbnm"
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend (sõna või lause): ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsontanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in märkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m} \nT: {t}")
else:
    print(f"kokku on {len(tekst_list)}")
    
