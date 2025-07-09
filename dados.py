import random

def jugada():
    jugadas = []
    for i in range(6):
        a = random.randint(1,6)
        jugadas.append(a)
        ultimas_jugadas = jugadas[-3:]
    return ultimas_jugadas
    
ultimas_jugadas = jugada()
print(ultimas_jugadas)