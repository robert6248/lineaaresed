#1 ülesanne
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
    
#5 ülesanne
n = int(input("Введите количество элементов: "))
elements = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]
m = int(input("Введите количество элементов, которые нужно поменять местами: "))
for i in range(m // 2):
    elements[i], elements[m - 1 - i] = elements[m - 1 - i], elements[i]
print("Изменённый список:", elements)

#6 ülesanne
n = int(input("Введите количество чисел: "))
numbers = []
for _ in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)
max_num = max(numbers)
length = len(numbers)
useless_number = max_num / length
numbers[numbers.index(max_num)] = useless_number
print("Обновлённый список:", numbers)

#7 ülesanne
n = int(input("Введите количество чисел: "))
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input(f"Введите число {i + 1}: "))
order = input("Введите порядок сортировки (возрастание или убывание): ")
if order == "возрастание": 
    numbers.sort(key=abs)
elif order == "убывание":
    numbers.sort(key=abs)
    numbers = numbers[::-1]
print("Отсортированный список:", numbers)
 
# 12 ülesanne
import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", numbers)
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print("Изменённый список:", numbers) 

# #16 ülesanne
import random
vastused = ["Jah, kindlasti", "Jah", "Võib-olla", "Ei"]
küsimus = input("Esita küsimus: ")
vastus = random.choice(vastused)
print("Vastus:", vastus)