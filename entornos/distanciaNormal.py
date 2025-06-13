import math
import matplotlib.pyplot as plt
from colorama import init, Fore, Style
init(autoreset=True) # Inicializa colorama para reiniciar colores automáticamente

x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

distanciaNormal = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(Fore.YELLOW + Style.BRIGHT + f"Distancia entre puntos: {distanciaNormal:.2f}")    

plt.scatter([x1, x2], [y1, y2], color='blue')
plt.plot([x1, x2], [y1, y2], color='gray', linestyle='--')
plt.text(x1, y1, 'P1')
plt.text(x2, y2, 'P2')
plt.title(f"Distancia = {distanciaNormal:.2f}")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
