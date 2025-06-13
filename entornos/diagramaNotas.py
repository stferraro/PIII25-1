import matplotlib.pyplot as plt

def diagrama_notas(notas: dict, color: str):
    """
    Dibuja un diagrama de barras de las notas de las asignaturas en el color dado.

    :param notas: Diccionario con asignaturas como claves y notas como valores.
    :param color: Cadena con el nombre del color para las barras.
    """
    asignaturas = list(notas.keys())
    valores = list(notas.values())
    plt.bar(asignaturas, valores, color=color)
    plt.xlabel("Asignaturas")
    plt.ylabel("Notas")
    plt.title("Diagrama de Notas")
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()