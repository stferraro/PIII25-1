tmax = float(input("Ingrese la temperatura máxima: "))
tmin = float(input("Ingrese la temperatura mínima: "))
tmedia = (tmax + tmin) / 2

grados_f = ((tmedia * 9 / 5) + 32)

print(f'La temperatura media es: {grados_f:.2f}')