años_experiencia = int(input("Ingrese los años de experiencia del trabajador: "))
bono_cursos = 0
cantidad_cursos = int(input("Ingrese la cantidad de cursos del trabajador: "))
bono_instructor = 0

if años_experiencia > 0 and años_experiencia <= 2:
    sueldo_base = 2500
elif años_experiencia >= 3 and años_experiencia <= 5:
    sueldo_base = 4000
else:
    sueldo_base = 6000

if cantidad_cursos >= 1 and cantidad_cursos <= 3:
    bono_cursos = 0
elif cantidad_cursos >= 4 and cantidad_cursos <= 6:
    bono_cursos = 0.08
elif cantidad_cursos >= 7 and cantidad_cursos <= 10:
    bono_cursos = 0.12
else:
    bono_cursos = 0.18
    
sueldo_cursos = sueldo_base + (sueldo_base * bono_cursos)

estudiantes_inscritos = int(input("Ingrese la cantidad de estudiantes inscritos: "))
if estudiantes_inscritos > 10 and estudiantes_inscritos <= 30:
    bono_estudiantes = 3000
elif estudiantes_inscritos > 30:
    bono_estudiantes = 6000
    
sexo_instructor = input("Ingrese el sexo del instructor(M o F): ")
edad_instructor = int(input("Ingrese la edad del instructor: "))

if sexo_instructor == "M" and edad_instructor >= 55:
    bono_instructor = 3500
elif sexo_instructor == "F" and edad_instructor >= 50:
    bono_instructor = 4500
    
DESC = 0.30

sueldo_total = sueldo_cursos + bono_estudiantes + bono_instructor
ganancia_total = sueldo_total - (sueldo_total * DESC)

print(f'La ganancia total es: {ganancia_total:.2f}')