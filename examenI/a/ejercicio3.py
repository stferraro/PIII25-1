tmax = float(input("Ingrese la temperatura máxima: "))
tmin = float(input("Ingrese la temperatura mínima: "))
tmedia = (tmax + tmin) / 2

grados_c = ((tmedia - 32 * 5) / 9)

print(f'La temperatura media es: {grados_c:.2f}')