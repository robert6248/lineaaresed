from datetime import *
from math import *
from time import strptime
from cgi import print_arguments
from datetime import *
from calendar import *
tana=date.today()
print(f"Tere! Täna on {tana}.")

# 27/12/2022 
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y") 
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)

päev=tana.day
kuu=tana.month
aasta=tana.year
print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
paevad=monthrange(2025,2)[1]
onjaanud=paevad-päev
print(f"Kuu lõpuni on jäänud {onjaanud} päevad")

päevad_aastal = (date(aasta, 12, 31) - tana).days
print(f"Kuni aasta lõpuni on jäänud {päevad_aastal} päevad")

try:
    sünnipäev=input("Sünnipäev: ") #YYYY-MM-DD
    sp=datetime.strptime(sünnipäev, "%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12
    print(f"Vastus: Vanus {vanus_aastades} aastad")
except:
    print("Sa pead YYYY-MM-DD format kasuada sisestamisel.")
   

# #ülesanne 2
#sulgude kasutamine

print("a=3 + 8 / (4-2) * 4")
a=3 + 8 / (4-2) * 4
print (a)
print("a=(3 + 8)/ (4 - 2) * 4")
a=(3 + 8) / (4 - 2) * 4
print (a)

#Ülesanne 3
try:
    R=float(input("Sisesta R, kus R on ringi raadius:"))
    #==,!=, <, >, <=, >=
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        Ringi_S=round(pi*R**2,2)
        Ringi_P=round(2*pi*R,2)
        Ruudsu_S=2*R*2*R
        Ruudu_P=4*2*R
        print(f"Ringi_S={Ringi_S}\nRingi_P={Ringi_P}\nRuudsu_S={Ruudsu_S}\nRuudu_P={Ruudu_P}")
except: 
    print("Sisesta ainult arvud!!!")

#ülesanne 4
maa_R_km=6378
münte_d=22.75
maa_R_mm=maa_R_km*1000000
maa_p=2*pi*maa_R_mm
münte_arv=round(maa_p/münte_d)
print(f"On vaja {münte_arv} münte")


# #ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(2*a,b,2*a,b,4*a)


#ülesanne 6
t="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(t.upper())

#ülesanne 7
a=float(input("Sisesta ristküliku esimene külje pikkus: "))
b=float(input("Sisesta ristküliku teine külje pikkus: "))
ümbermõõt=2*(a+b)
pindala=(a*b)
print(f"ristlikku ümbermõõt on {ümbermõõt}, ja pindala on {pindala}.")


# Ülesanne 8
kütus_litr=float(input("sisesta tangitud kütuse kogus: "))
läbitud_km=float(input("sisesta läbitud km: "))
if läbitud_km>0:
# kütuse_kulu kütus_litr/läbitud_km*100
    print(f"keskmine kütusekulu on {kütuse_kulu} liitrit.")
else:
    print(f"viga: läbitud km arv peab olema suurem kui 0.")



#ülesanne 9
kiirus = 29.9 
minutid = float(input("Sisesta minutid: "))
distants = kiirus * minutid / 60  
print(f"Rulluisutaja jõuab {distants} km {minutid} minutiga.")
# ülesanne 10     
minutid_kasutajalt=int(input("Aeg minutides"))
tunnid=minutid_kasutajalt//60
minutid=minutid_kasutajalt%60
print("vastus".center(20,"*"))