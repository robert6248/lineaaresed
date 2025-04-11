
from random import *
from math import *
#ülesanne 1
nimi=input("Mis on sinu nimi?: ")
vanus=int(input("Kui vana sa oled?: "))

print(f"Tere, maailm! Tervitan sind {nimi} Sa oled {vanus} aastat vana. ")
print("Tere, maailm! Tervitan sind" ,nimi, "Sa oled",vanus,"aastat vana.")
print("Tere, maailm! Tervitan sind"+nimi+"Sa oled"+str(vanus)+"aastat vana")
#ülesanne 2
from re import Match
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(f"Muutuja {vanus} on {type(vanus)} tüübi") 
print(f"Muutuja {eesnimi} on {type(eesnimi)} tüübi") 
print(f"Muutuja {pikkus} on {type(pikkus)} tüübi")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)} tüübi")
#ülesanne 3
kommidearv=randint(1,100)
print(f"Laual on {kommidearv} kommid")
kommidvõtmud=int(input("Mitu kommi tahad ära võtta?"))
onjäänud=kommidearv-kommidvõtmud
print(f"Laual on jäänud{onjäänud} komme")
#ülesanne 4
ümbermõõt=int(input("kui suur on ümbermõtt: "))
läbimõõt=ümbermõõt//pi
print(f"läbimõõt on +f{läbimõõt}")
#ülesanne 5
N=float(input("Sisesta ristküliku pikkus(N): "))
M=float(input("Sisesta ristküliku laius (M): "))
diagonaal=sqrt(N**2 + M**2)
print(diagonaal)
#ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")
#ülesanne 7
a1=randint(0,100)
a2=randint(0,100)
a3=randint(0,100)
a4=randint(0,100)
a5=randint(0,100)
keskmine=(a1+a2+a3+a4+a5)/5
print(f"Arvud olid: {a1}, {a2}, {a3}, {a4}, {a5}. Nende keskmine on {keskmine}")
#ülesanne 8
tekst= """ 
    @..@
   (----)
  ( \__/ )
  ^^ "" ^^ """
print(tekst)

print(      "@..@")
print(     "(----)")
print(    "( \__/ )")
print("""  ^^ "" ^^   """)  

#ülesanne 9
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
P=a+b+c 
print(f"a={a}, b={b}, c={c}, P={P}")
#ülesanne 10
pitsa = 12.90
hind = pitsa * 1.10
person=randint(1,5)
hind_na_person=hind/person
print(f"pitsa={pitsa}, hind={hind}, hind_na_person={hind_na_person}, person={person}")
