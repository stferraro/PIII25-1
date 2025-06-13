import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Ingresa el número de años: "))

anios = np.arange(2024 - n + 1, 2025)
pib = np.linspace(300, 300 + (n - 1) * 10, n) 


df = pd.DataFrame({'Año': anios, 'PIB': pib})

df['Crecimiento (%)'] = df['PIB'].pct_change() * 100

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(df['Año'], df['PIB'], marker='o', color='green')
plt.title('PIB')
plt.xlabel('Año')
plt.ylabel('PIB (miles de millones)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(df['Año'][1:], df['Crecimiento (%)'][1:], color='blue')
plt.title('Crecimiento (%)')
plt.xlabel('Año')
plt.ylabel('Crecimiento')
plt.grid(True)

plt.tight_layout()
plt.show()


