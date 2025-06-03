import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.title("prillid")
#1
x1 = np.linspace(-9, -1, 400)
y1 = -(1/16)*(x1 + 5)**2 + 2
plt.plot(x1, y1, color='purple')
#2
x2 = np.linspace(1, 9, 400)
y2 = -(1/16)*(x2 - 5)**2 + 2
plt.plot(x2, y2, color='brown')
#3
x3 = np.linspace(-9, -1, 400)
y3 = (1/4)*(x3 + 5)**2 - 3
plt.plot(x3, y3, color='blue')
#4
x4 = np.linspace(1, 9, 400)
y4 = (1/4)*(x4 - 5)**2 - 3
plt.plot(x4, y4, color='orange')
#5
x5 = np.linspace(-9, -6, 200)
y5 = -(x5 + 7)**2 + 5
plt.plot(x5, y5, color='violet') 
#6
x6 = np.linspace(6, 9, 200)
y6 = -(x6 - 7)**2 + 5
plt.plot(x6, y6, color='brown')
#7
x7 = np.linspace(-1, 1, 200)
y7 = -0.5 * x7**2 + 1.5
plt.plot(x7, y7, color='green')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()

