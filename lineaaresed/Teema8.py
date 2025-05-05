import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10,1)
y=2*x**2-4*x+5
plt.plot(x,y)
plt.xlabel('X-telg')
plt.ylabel('y=2*x**2-4*x+5')
plt.title('Graafik')
plt.figure(facecolor='yellow')
plt.grid()
plt.savefig('graafik.png')
plt.show()



x=[1, 2, 3, 4, 5]
y=[10,20,25,30,35]
plt.plot(x, y,linestyle="--",marker="D",markersize=10,color="darkblue")
plt.xlabel('X-telg')
plt.ylabel('Y-telg')
plt.title('Lihtne graafik')
plt.show()

plt.scatter(x, y, color='lightblue',label="Punktidest diagramm")
plt.show()

plt.bar(x, y, color='darkred', label="Tulpdiagramm")
plt.legend()
plt.show()

plt.scatter(x, y, color='blue', label="diagramm")
plt.show()


