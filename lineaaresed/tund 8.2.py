import numpy as np
import matplotlib.pyplot as plt

#1 
nimed = []
korgused = []

with open("maed.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split()
        nimi = " ".join(osad[:-1])
        korgus = int(osad[-1])
        nimed.append(nimi)
        korgused.append(korgus)

#2 
korgused_np = np.array(korgused)
keskmine = np.mean(korgused_np)
korgeim = np.max(korgused_np)
madalaim = np.min(korgused_np)
kogusumma = np.sum(korgused_np)

#3 
print("Keskmine kõrgus:", keskmine, "m")
print("Kõrgeim mägi:", nimed[np.argmax(korgused_np)], "-", korgeim, "m")
print("Madalaim mägi:", nimed[np.argmin(korgused_np)], "-", madalaim, "m")
print("Kogusumma:", kogusumma, "m")

# 4 
plt.figure(figsize=(10, 6))
plt.bar(nimed, korgused, color="skyblue") 
plt.xlabel("Mäed")
plt.ylabel("Kõrgus (m)")
plt.title("Mägede kõrgused")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik.png") 
plt.show()

nimed_sorted, korgused_sorted = zip(*sorted(zip(nimed, korgused), key=lambda x: x[1], reverse=True))

plt.figure(figsize=(10, 6))
plt.bar(nimed_sorted, korgused_sorted, color="orange")
plt.xlabel("Mäed (sorteeritud)")
plt.ylabel("Kõrgus (m)")
plt.title("Mägede kõrgused (kahanev)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("maed_graafik_sorteeritud.png")
plt.show()
