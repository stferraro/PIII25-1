def datos_usuario():
    usuarios = {}
    cedula = input("Ingrese su cédula: ")
    while cedula != "fin":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        while edad < 0:
            edad = int(input("Edad inválida. Ingrese su edad: "))
        membresia = input("Ingrese el tipo de membresía (Mensual, Semestral, Anual): ")
        while membresia not in ["Mensual", "Semestral", "Anual"]:
            membresia = input("Tipo de membresía inválido. Ingrese el tipo de membresía (Mensual, Semestral, Anual): ")
        usuarios[cedula] = {
            "nombre": nombre,
            "edad": edad,
            "membresia": membresia
        }
        cedula = input("Ingrese su cédula (o 'fin' para terminar): ")
        if cedula == "fin":
            break
    return usuarios

def get_valor_mensualidad(datos_usuario):
    valor_mensualidad = 0
    cedula = input("Ingrese su cédula: ")
    if cedula in datos_usuario.keys():
        print(f"Nombre: {datos_usuario[cedula]['membresia']}")
        if datos_usuario.get(cedula).get('membresia') == "Mensual":
            valor_mensualidad = 20
        elif datos_usuario.get(cedula).get('membresia') == "Trimestral":
            valor_mensualidad = 55
        elif datos_usuario.get(cedula).get('membresia') == "Anual":
            valor_mensualidad = 200
    else:
        print("Cédula no encontrada.")
    return valor_mensualidad

def main():
    usuarios = datos_usuario()
    valor_mensualidad = get_valor_mensualidad(usuarios)
    print(f"Valor de la mensualidad: {valor_mensualidad}")
    
main()