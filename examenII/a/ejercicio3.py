sueldo_base = 0
años_experiencia = int(input("Ingrese los años de experiencia del trabajador: "))
bono_compesacion = 0
monto_vendido = float(input("Ingrese el monto vendido por el trabajador: "))
bono_hijos = 0
cantidad_hijos = int(input("Ingrese la cantidad de hijos del trabajador: "))
sexo_trabajador = input("Ingrese el sexo del trabajador(M o F): ")
edad = int(input("Ingrese la edad del trabajador: "))
bono_edad = 0
DESC_GUBER = 0.33

if años_experiencia > 0 and años_experiencia <= 3:
    sueldo_base = 2000
elif años_experiencia > 4 and años_experiencia <= 6:
    sueldo_base = 3500
else:
    sueldo_base = 5000
    
if monto_vendido > 0 and monto_vendido <= 25000:
    bono_compesacion = 0
elif monto_vendido > 250000 and monto_vendido <= 40000:
    bono_compesacion = 0.05
elif monto_vendido > 400000 and monto_vendido <= 80000:
    bono_compesacion = 0.10
else:
    bono_compesacion = 0.15

sueldo_comp = monto_vendido + (monto_vendido * bono_compesacion)

if cantidad_hijos >= 1 and cantidad_hijos <= 3:
    bono_hijos = 2000
else:
    bono_hijos = 5000
    
if sexo_trabajador == "M" and edad > 60:
    bono_edad = 4000
elif sexo_trabajador == "F" and edad > 55:
    bono_edad = 5000
    
sueldo_total = sueldo_base + sueldo_comp + bono_hijos + bono_edad
ganancia_total = sueldo_total - (sueldo_total * DESC_GUBER)

print(f'La ganancia total del trabajador es: {ganancia_total:.2f}')

