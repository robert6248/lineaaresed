# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# for i in range(0,10,1):
#     print(f"{i+1}. samm")
# for i in range(1,11):
#     print(f"{i}. samm")

# #1 ülesanne
# while True:
#     try:
#         nimi=(input("Mis on sinu nimi?: "))
#         if nimi.isalpha(): break
#     except:
#         print("Viga!")
# while True:
#     try:
#         k=int(input("Mitu korda tervitada?: "))
#         if k>0: break
#     except:
#         print("Viga!")
# #1. variant
# i=0
# while True:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
#     if i==k: break
# i=0
# while i<k:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
# #2. variant
# print("while tingimusega")
# i=0
# while i<k:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
# #3. variant
# print("For")
# for i in range (1,k+1):
#     print(f"Ole tervitatud, {nimi}, {i}. korda")

# from keyboard import *
#2 ülesanne

# #1. variant
# summa = 0
# j=0
# while True:
#     while True:
#         try:
#            a=float(input("a: "))
#            break
#         except:
#             print("Viga!")
#     summa+=a
#     j+=1
#     if j==10: break
# print(f"Arvude summa {summa}")

# #2. variant
# summa = 0
# while True:
#     number = input("Sisesta arv (või vajuta Enter, et lõpetada): ")
#     if number == "": break
#     try:
#         summa += float(number)
#         summa += number
#     except:
#         print("Viga")
# print("Arvude summa on:", {summa})


from random import *
#3 ülesanne
for küsimuse_nr in range(10):
    a=randint(1,50)
    b=randint(1,50)
    õige_vastus=a+b
    print(f"{a}+{b}", end="")
    p=0
    õ=0
    vastus=0
    while p<5 and vastus!=õige_vastus: 
        vastus=int(input("="))
        if vastus==õige_vastus:
            print("Tubli!") 
            õ+=1
        p+=1
    print(f"Õige vastus: {õige_vastus}")
print("Vale")
 
# #5 ülesanne
# N = int(input("Sisesta suurus (N): "))
# for j in range(N):
#     for i in range(N):
#         if i == j or i==N-j-1:
#             print("X", end=" ")
#         else:7
#             print("O", end=" ")
#     print()
# print()
# #6 ülesanne
 
# #7 ülesanne
# N=1
# for i in range(4):
#     N*=10
#     print(N)
#     N+=randint(0,9)
#     print(N)