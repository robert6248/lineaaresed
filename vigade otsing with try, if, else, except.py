import math  # импортируем math для использования математических функций

# ------------------
print("Ruudu karakteristikud")
try:
    a = int(input('Sisesta ruudu külje pikkus => '))
    if a > 0:
        S = a**2
        print(f"Ruudu pindala, {S}")
        P = 4 * a
        print(f"Ruudu ümbermõõt, {P}")
        di = a * math.sqrt(2)
        print(f"Ruudu diagonaal, {round(di, 2)}")
    else:
        print("Külg ei saa olla <=0-ga")
except:
    print("Külje suurus on vaja int formaadis sisestada!")
# ----------------------
print("Ristküliku karakteristikud")
try:
    b = int(input("Sisesta ristküliku 1. külje pikkus => "))
    c = int(input("Sisesta ristküliku 2. külje pikkus => "))
    
    if b <= 0 or c <= 0:
        print("Küljed peavad olema positiivsed numbrid.")
    else:
        S = b * c
        print(f"Ristküliku pindala, {S}")
        
        P = 2 * (b + c)
        print(f"Ristküliku ümbermõõt, {P}")
        
        di = math.sqrt(b**2 + c**2)  
        print(f"Ristküliku diagonaal, {round(di)}")
except:
    print("Viga: Palun sisestage numbrilised väärtused!")
# ----------------------
print("Ringi karakteristikud")
try:
    r = int(input("Sisesta ringi raadiusi pikkus => "))
    
    if r <= 0:
        print("Raadius peab olema positiivne number.")
    else:
        d = 2 * r
        print(f"Ringi läbimõõt, {d}")
        
        S = math.pi * r**2
        print(f"Ringi pindala, {round(S)}")
        
        C = 2 * math.pi * r
        print(f"Ringjoone pikkus, {round(C)}")
except:
    print("Viga: Palun sisestage numbrilised väärtused!")
