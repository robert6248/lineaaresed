import math

print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu külje pikkus => "))
S = a**2
P = 4 * a
di = a * math.sqrt(2)
print("Ruudu pindala", S)
print("Ruudu ümbermõõt", P)
print("Ruudu diagonaal", round(di, 2))


print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b * c 
P = 2 * (b + c)
di = math.sqrt(b**2 + c**2) 
print("Ristküliku pindala", S)
print("Ristküliku ümbermõõt", P)
print("Ristküliku diagonaal", round(di, 2))

 
print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiusi pikkus => "))
d = 2 * r
S = math.pi * r**2
C = 2 * math.pi * r
print("Ringi läbimõõt", d)
print("Ringi pindala", round(S, 2))
print("Ringjoone pikkus", round(C, 2))
