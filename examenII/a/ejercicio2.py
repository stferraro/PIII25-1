sueldo_base = 0
años_experiencia = int(input("Ingrese los años de experiencia del trabajador: "))
certificaciones = int(input("Ingrese la cantidad de certificaciones del trabajador: "))
bono_certificaciones = 0
bono_capacitacion = 0
horas_capacitacion = float(input("Ingrese las horas de capacitación del trabajador: "))
bono_dependientes = 0
cantidad_dependientes = int(input("Ingrese la cantidad de dependientes del trabajador: "))
bono_ubicacion = 0
costo_ubicacion = input("Ingrese el costo de ubicación del trabajador: ")
TOT_GASTOS = 1200+1800
sueldo_total_mensual_mensual = 0
ganancia_mensual = 0

if años_experiencia > 0 and años_experiencia <= 2:
    sueldo_base = 2800
elif años_experiencia > 2 and años_experiencia <= 5:
    sueldo_base = 3700
else:
    sueldo_base = 5000

if certificaciones == 1:
    bono_certificaciones = 0.05
elif certificaciones == 2:
    bono_certificaciones = 0.10
elif certificaciones > 2:
    bono_certificaciones = 0.15

sueldo_cert = sueldo_base + (sueldo_base * bono_certificaciones)

if horas_capacitacion > 30:
    bono_capacitacion = 0.25
elif horas_capacitacion <= 30 and horas_capacitacion >= 15:
    bono_capacitacion = 0.15
elif horas_capacitacion < 15 and horas_capacitacion > 5:
    bono_capacitacion = 0.07
else:
    bono_capacitacion = 0
sueldo_cap = sueldo_cert + (sueldo_cert * bono_capacitacion)

if cantidad_dependientes > 1 and cantidad_dependientes <= 2:
    bono_dependientes = 0.06
else:
    bono_dependientes = 0.12
    
sueldo_dependientes = sueldo_cap + (sueldo_cap * bono_dependientes)

if costo_ubicacion == "Alto":
    bono_ubicacion = 0.20
elif costo_ubicacion == "Medio":
    bono_ubicacion = 0.10
else:
    bono_ubicacion = 0

sueldo_ubicacion = sueldo_dependientes + (sueldo_dependientes * bono_ubicacion)

sueldo_total_mensual = sueldo_base + sueldo_cert + sueldo_cap + sueldo_dependientes + sueldo_ubicacion
ganancia_mensual = sueldo_total_mensual - TOT_GASTOS

if ganancia_mensual > 3000:
    print('el trabajador puede compra el equipo de trabajo con costo mayor a 3000$')
else:
    print('el trabajador no puede compra el equipo de trabajo con costo mayor a 3000$')
    
    


   

