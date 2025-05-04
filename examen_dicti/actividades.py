def datos():
    cedula = input("Ingrese su cédula: ")
    nombre = input("Ingrese su nombre: ")
    datos = {
        "cedula": cedula,
        "nombre": nombre
    }
    return datos

def actividades():
    actividades = {}
    descripcion = input("Ingrese la descripción de la actividad: ")
    while descripcion != "fin":
        horas = float(input("Ingrese las horas de la actividad: "))
        while horas < 0:
            horas = float(input("Horas inválidas. Ingrese las horas de la actividad: "))
        actividades[descripcion] = horas
        descripcion = input("Ingrese la descripción de la actividad (o 'fin' para terminar): ")
        if descripcion == "fin":
            break
    return actividades

def asigna_actividad(datos, actividades):
    actividad_asignada = {}
    actividad = input("Ingrese la actividad a asignar: ")
    if actividad in actividades.keys():
        actividad_asignada[actividad] = datos
        print(f"Actividad '{actividad}' asignada a {datos['nombre']}")
    else:
        print("Actividad no encontrada. Intenta nuevamente.")
    return actividad_asignada

def main():
    datos_usuario = datos()
    actividades_usuario = actividades()
    actividad_asignada = asigna_actividad(datos_usuario, actividades_usuario)
    print(f"Actividad asignada: {actividad_asignada}")
    
main()