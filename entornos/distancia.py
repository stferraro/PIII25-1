import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from colorama import init, Fore, Style
init(autoreset=True) # Inicializa colorama para reiniciar colores automáticamente

x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

datos = {
    'x': [x1, x2],
    'y': [y1, y2]
}
df = pd.DataFrame(datos)

p1 = df.iloc[0].values
p2 = df.iloc[1].values
distancia = np.linalg.norm(p2 - p1)
distanciaNormal = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print(f"Distancia calculada con numpy: {distancia:.2f}")
print(f"Distancia calculada manualmente: {distanciaNormal:.2f}")

print(Fore.YELLOW + Style.BRIGHT + f"Distancia entre puntos: {distancia:.2f}")

plt.scatter(df['x'], df['y'], color='blue')
plt.plot(df['x'], df['y'], color='gray', linestyle='--')
plt.text(df['x'][0], df['y'][0], 'P1')
plt.text(df['x'][1], df['y'][1], 'P2')
plt.title(f"Distancia = {distancia:.2f}")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
