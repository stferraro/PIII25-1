nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
cedula = input("Ingrese su cedula: ")

valor_hora = float(input("Ingrese el valor de la hora: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

salario = valor_hora * horas_trabajadas

print(f'El salario de {nombre} {apellido} con cedula {cedula} es: {salario:.2f}')