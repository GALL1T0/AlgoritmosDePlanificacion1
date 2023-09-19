class Proceso:
    def __init__(self, nombre, tiempo, prioridad):
        self.nombre = nombre
        self.tiempo = tiempo
        self.prioridad = prioridad

# Función para simular el algoritmo Round Robin
def round_robin(procesos, quantum):
    # Copiamos la lista de procesos para no modificarla
    procesos = procesos.copy()
    tiempo_total = 0
    resultado = []

    while procesos:
        proceso_actual = procesos.pop(0)
        if proceso_actual.tiempo > quantum:
            proceso_actual.tiempo -= quantum
            tiempo_total += quantum
            procesos.append(proceso_actual)
        else:
            tiempo_total += proceso_actual.tiempo
            resultado.append((proceso_actual.nombre, tiempo_total))

    return resultado

# Función para simular el algoritmo SJF
def sjf(procesos):
    procesos.sort(key=lambda x: x.tiempo)
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        tiempo_total += proceso.tiempo
        resultado.append((proceso.nombre, tiempo_total))

    return resultado

# Función para simular el algoritmo FIFO
def fifo(procesos):
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        tiempo_total += proceso.tiempo
        resultado.append((proceso.nombre, tiempo_total))

    return resultado

# Función para simular el algoritmo de prioridades
def prioridades(procesos):
    procesos.sort(key=lambda x: x.prioridad)
    tiempo_total = 0
    resultado = []

    for proceso in procesos:
        tiempo_total += proceso.tiempo
        resultado.append((proceso.nombre, tiempo_total))

    return resultado

# Definimos los procesos
procesos = [
    Proceso("Google Chrome", 11, 2),
    Proceso("Slack", 8, 3),
    Proceso("Registry", 6, 7),
    Proceso("Inicio", 3, 5),
    Proceso("Shell", 6, 3),
    Proceso("Host de Servicio", 10, 1),
    Proceso("Microsoft Text", 7, 2),
    Proceso("System", 8, 4),
    Proceso("Wininit", 1, 1),
    Proceso("smss", 2, 3)
]

# Simulamos los algoritmos y escribimos los resultados en archivos de texto
algoritmos = [round_robin, sjf, fifo, prioridades]
nombres_algoritmos = ["Round Robin", "SJF", "FIFO", "Prioridades"]
quantum = 3  # Quantum para Round Robin

for i, algoritmo in enumerate(algoritmos):
    if algoritmo == round_robin:
        resultado = algoritmo(procesos.copy(), quantum)  # Pasa el quantum como argumento
    else:
        resultado = algoritmo(procesos.copy())
    with open(f"{nombres_algoritmos[i]}.txt", "w") as archivo:
        for proceso, tiempo in resultado:
            archivo.write(f"{proceso}: Tiempo total = {tiempo} unidades de tiempo\n")
