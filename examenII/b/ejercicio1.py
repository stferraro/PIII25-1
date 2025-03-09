cargo_empleado = input("Ingrese el cargo del empleado(Junior, SemiSenior, Senior): ")
evaluacion_mensual = float(input("Ingrese la evaluación mensual del empleado: "))
cantidad_proyectos = int(input("Ingrese la cantidad de proyectos del empleado: "))
bono_proyectos = 0
km_distacia = float(input("Ingrese la distancia de viaje del empleado: "))
bono_distancia = 0
TOT_GASTOS = 1300+1500+500


match cargo_empleado:
    case "Junior":
        sueldo_base = 2500
    case "SemiSenior":
        sueldo_base = 4000
    case "Senior":
        sueldo_base = 6000
    case _:
        print("Cargo no válido")
        
if evaluacion_mensual > 90:
    bono_evaluacion = 0.20
elif evaluacion_mensual < 90 and evaluacion_mensual > 80:
    bono_evaluacion = 0.10
elif evaluacion_mensual < 80 and evaluacion_mensual > 70:
    bono_evaluacion = 0.05
else:
    bono_evaluacion = 0
    
sueldo_comp = sueldo_base + (sueldo_base * bono_evaluacion)

if cantidad_proyectos >= 5:
    bono_proyectos = 0.18
elif cantidad_proyectos >= 3 and cantidad_proyectos < 5:
    bono_proyectos = 0.12
else:
    bono_proyectos = 0.05

sueldo_proyectos = sueldo_base + (sueldo_base * bono_proyectos)

if km_distacia > 30:
    bono_distancia = 0.15
elif km_distacia > 15 and km_distacia <= 30:
    bono_distancia = 0.08
else:
    bono_distancia = 0

sueldo_distancia = sueldo_base + (sueldo_base * bono_distancia)

sueldo_total_mensual = sueldo_base + sueldo_comp + sueldo_proyectos + sueldo_distancia
ganancia_total = sueldo_total_mensual - TOT_GASTOS

if ganancia_total > 2800:
    print('el trabajador puede realizar la certificación profesional')
else:
    print('el trabajador no puede realizar la certificación profesional')
