def agrega_habitaciones():
    habitaciones={}
    numero = input('Numero habitacion(fin para cerrar): ')
    while numero != 'fin':
        estado = input('disponible/ocupada: ')
        while estado not in ('disponible', 'ocupada'):
            estado = input(bool('disponible/ocupada: '))
        habitaciones[numero] = estado
        numero = input('Numero habitacion(fin para cerrar): ')
        if numero == 'fin':
            break
    return habitaciones

def registra_usuarios():
    usuarios = {}
    entrada = input('Quieres Registrar un usuario: (s/n)')
    while True:
        nombre_completo = input('Nombre: ')
        cedula = input('Cedula: ')
        telefono = input('Telefono: ')
        usuarios[cedula] = {
            'Nombre': nombre_completo,
            'cedula': cedula,
            'telefono': telefono
        }
        entrada = input('Quieres Registrar un usuario: (s/n)')
        if entrada.lower() == 'n':
            break
    return usuarios
    
    
def asigna_habitacion(habitaciones, usuarios):
    datos_habitacion = {}
    while True:
        numero = input('Numero habitacion (fin para cerrar): ')
        if numero == 'fin':
            break  

        estado = habitaciones.get(numero)
        if estado is None:
            print("Habitación no registrada. Intenta con otra.")
            continue 

        if estado == 'disponible':
            cedula = input('Cedula: ')
            if cedula in usuarios.keys():
                datos_habitacion[cedula] = {
                    'Nombre': usuarios[cedula]['Nombre'],
                    'Habitacion': numero
                }
                habitaciones[numero] = 'ocupada'  
                print(f"Habitación {numero} asignada a {usuarios[cedula]['Nombre']}")
                break 
            else:
                print("Cédula no encontrada. Intenta nuevamente.")
        else:
            print("Habitación ocupada. Intenta con otra.")
    return datos_habitacion

usuarios = registra_usuarios()
habitaciones = agrega_habitaciones()
asignadas = asigna_habitacion(habitaciones, usuarios)
print(asignadas)

        