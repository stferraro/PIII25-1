def pedir_datos():
    nombre = input('Nombre Estudiante: ')
    apellido = input('Apellido: ')
    cedula = input('Cedula: ')
    codigo_universitario = input('Codigo Universitario: ')
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'cedula': cedula,
        'codigo_universitario': codigo_universitario
    }
    
def llena_dict_notas():
    dict_notas = {}
    materia = input('Materia(n para salir): ')
    while materia != 'n':
        nota = float(input('Nota: '))
        while nota < 0 or nota > 20:  # Assuming valid grades are between 0 and 20
            print("Nota inválida. Debe estar entre 0 y 20.")
            nota = float(input('Nota: '))
        dict_notas[materia] = nota
        materia = input('Materia(n para salir): ')
        if materia == 'fin':
            break
    return dict_notas

def calcula_promedio(notas):
    return sum(notas.values())/len(notas.values())

def verifica_aprobacion(promedio):
    if promedio >= 10:
        return 'Semestre Aprobado'
    else:
        return 'Semestre no Aprobado' 
        
def main():
    usuario = pedir_datos()
    print(usuario)
    notas = llena_dict_notas()
    print(notas)
    promedio = calcula_promedio(notas)
    print(promedio)
    print(verifica_aprobacion(promedio))
    
main()