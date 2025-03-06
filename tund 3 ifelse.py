# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#    print(f"Korrutis võrdub: {a*b}")

# #kas a on paaris või paaritu arv?
# if a%2==0 and a!=0:
#     print(f"Arv {a} on paaris")
# elif a==0:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"Arv {a} on paaritud")

#Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("Mis hinne sai täna koolis?: "))
#     if hinne in range(1,6):
#         print("Hinne")
#     if hinne<=2:
#         print(f"Miks on {hinne}!?!?!")
#     if hinne==5:
#         print("hästi")
#     elif hinne==4:
#         print("hästi")
#     elif hinne==3:
#         print("enam vähem")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga:", e)


# nimi="PYTHON"
# print(nimi.isupper())
# if nimi.isupper():
#     print("Suured tähed")
# else:
#     print("Ei ole kõik suured tähed")

#ülesanne
#1 Juku
# nimi = input("Mis on sinu nimi? ")

# if nimi="JUKU":
#     print("Lähme kinno!")
#     try:
#         vanus = int(input("Kui vana sa oled? "))
#         if vanus < 0 or vanus > 100:
#             print("Viga andmetega.")
#         elif vanus <= 6:
#             print("Pilet: Tasuta")
#         elif vanus <= 14:
#             print("Pilet: Lastepilet")
#         elif vanus <= 60:
#             print("Pilet: Täispilet")
#         else:
#             print("Pilet: Sooduspilet")
#     except:
#         print("Palun sisesta kehtiv täisarv.")
# else:
#     print("Ma olen hõivatud! Mine kinno ise!")

#2 pinginaabrid
#Robert Ruslan Bohdan
# nimed=["Robert","Ruslan","Bohdan"]
# nimi1=input()
# nimi2=input()
# nimi3=input()
# if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
#     print ("Pinginaabrid")
# else:
#     print("Ei ole pinginaabrid")


#3 remont
# try:
#     a = float(input("Sisesta pikkus: "))
#     b = float(input("Sisesta laius: "))
#     #--------
#     S = a * b
#     soov = input("Kas sa tahad remondi teha?: ")
#     if soov.lower() == "jah":
#         print("Remont")
#         hind = float(input("Hind: "))
#         #--------
#         koguhind = S * hind
#         print(f"Sul on vaja {koguhind} eur")
#     elif soov.lower() == "ei":
#         print("Head aega!")
#     else:
#         print("Palun sisesta jah või ei!")
# except:
#     print("Pikkus, laius ja hind peavad olema numbrid!")


#
