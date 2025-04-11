a=float(input("A: "))
b=float(input("B: "))
if a>0 and b>0:
   print(f"Korrutis võrdub: {a*b}")

#kas a on paaris või paaritu arv?
a=float(input("A: "))
if a%2==0 and a!=0:
    print(f"Arv {a} on paaris")  
elif a==0: 
    print(f"Arv {a} on märamatu") 
else:
    print(f"Arv {a} on paaritud")

#Ema-robot 5-, 4-, 3-, 2-, 1-
try:
    hinne=int(input("Mis hinne sai täna koolis?: "))
    if hinne in range(1,6):
        print("Hinne")
    if hinne<=2:
        print(f"Miks on {hinne}!?!?!")
    if hinne==5:
        print("hästi")
    elif hinne==4:
        print("hästi")
    elif hinne==3:
        print("enam vähem")
    else:
        print("Ei ole hinne")
except Exception as e:
    print("Viga:", e)


nimi="PYTHON"
print(nimi.isupper())
if nimi.isupper():
    print("Suured tähed")
else:
    print("Ei ole kõik suured tähed")

#ülesanne 1
#Juku
nimi = input("Mis on sinu nimi? ")
if nimi=="JUKU":
    print("Lähme kinno!")
    try:
        vanus = int(input("Kui vana sa oled? "))
        if vanus < 0 or vanus > 100:
            print("Viga andmetega.")
        elif vanus <= 6:
            print("Pilet: Tasuta")
        elif vanus <= 14:
            print("Pilet: Lastepilet")
        elif vanus <= 60:
            print("Pilet: Täispilet")
        else:
            print("Pilet: Sooduspilet")
    except:
        print("Palun sisesta kehtiv täisarv.")
else:
    print("Ma olen hõivatud! Mine kinno ise!")

# 2 pinginaabrid
# Robert Ruslan Bohdan
nimed=["Robert","Ruslan","Bohdan"]
nimi1=input()
nimi2=input()
nimi3=input()
if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
    print ("Pinginaabrid")
else:
    print("Ei ole pinginaabrid")


# 3 remont
try:
    a = float(input("Sisesta pikkus: "))
    b = float(input("Sisesta laius: "))
    #--------
    S = a * b
    soov = input("Kas sa tahad remondi teha?: ")
    if soov.lower() == "jah":
        print("Remont")
        hind = float(input("Hind: "))
        #--------
        koguhind = S * hind
        print(f"Sul on vaja {koguhind} eur")
    elif soov.lower() == "ei":
        print("Head aega!")
    else:
        print("Palun sisesta jah või ei!")
except:
    print("Pikkus, laius ja hind peavad olema numbrid!")


# #ülesanne 4
alghind = float(input("Sisesta toode alghind: "))
if alghind > 700:
    soodus = alghind * 0.70  
    print(f"Soodus hind on {soodus} eurot.")
else:
    print("Soodustus ei kehti")


# ülesanne 5 temperatuur
temperatuur = float(input("Mis on praegune temperatuur? "))

if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, see on soe!")
else:
    print("Temperatuur on alla 18 kraadi, võib olla on jahe.")

#ülesanne 6 pikkus
pikkus = float(input("Mis on sinu pikkus (cm)? "))

if pikkus < 160:
    print("Oled lühike.")
elif 160 <= pikkus <= 180:
    print("Oled keskmine.")
else:
    print("Oled pikk.")

#Ülesanne 7
pikkus = float(input("Mis on sinu pikkus (cm)? "))
sugu = input("Mis on sinu sugu (Mees või Naine)? ").lower()

if sugu == "mees":
    if pikkus < 170:
        print("Oled lühike.")
    elif pikkus <= 185:
        print("Oled keskmine.")
    else:
        print("Oled pikk.")
elif sugu == "naine":
    if pikkus < 160:
        print("Oled lühike.")
    elif pikkus <= 175:
        print("Oled keskmine.")
    else:
        print("Oled pikk.")
else:
    print("Vigane sisend.")


#Ülesanne 8
import random
tooted = {
    "piim": random.randint(1, 8),
    "saia": random.randint(1, 5),  
    "leib": random.randint(1, 6)
}
total = 0
for toode, hind in tooted.items():
    count = int(input(f"Kui palju {toode} tahad osta? (hind: {hind} €): "))
    total += hind * count
print(f"Kokku: {total} €")
