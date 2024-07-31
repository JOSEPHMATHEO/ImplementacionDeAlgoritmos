import networkx as nt
import matplotlib.pyplot as mt


def grafo_archivo(ruta_archivo):
    grafo = nt.Graph()
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar espacios en blanco
            parts = linea.split(',')  # Separar los atributos por ','
            u = parts[0]
            v = parts[1]
            weight = int(parts[2])
            grafo.add_edge(u, v, weight=weight)  # Añadir arista al grafo
    return grafo

# Ruta del archivo que contiene el grafo
ruta = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//Grafo50.txt'
g = grafo_archivo(ruta)

# Función para crear un diccionario de índices si los nodos son cadenas
def crear_indices(graph):
    indices = {nodo: i for i, nodo in enumerate(graph.nodes)}
    return indices

# Creación de diccionario de índices
indices = crear_indices(g)

# Función para encontrar el conjunto al que pertenece un nodo
def buscar(conjunto, i):
    if conjunto[i] == i:
        return i
    else:
        return buscar(conjunto, conjunto[i])

# Función para unir dos conjuntos
def fusionar(conjunto, u, v):
    conjunto[buscar(conjunto, u)] = buscar(conjunto, v)

# Implementación del algoritmo de Kruskal
def kruskal(grafo):
    arm = nt.Graph()  # Grafo para el Árbol de Recubrimiento Mínimo
    aristas = sorted(grafo.edges(data=True), key=lambda x: x[2]['weight'])  # Ordenar aristas por peso
    conjunto = [i for i in range(len(grafo.nodes))]  # Crear conjuntos individuales para cada nodo

    for arista in aristas:
        n1, n2, peso = arista
        compu = buscar(conjunto, indices[n1])  # Encontrar conjunto de n1
        compv = buscar(conjunto, indices[n2])  # Encontrar conjunto de n2

        if compu != compv:
            fusionar(conjunto, indices[n1], indices[n2])  # Unir conjuntos
            arm.add_edge(n1, n2, weight=arista[2]['weight'])  # Añadir arista al ARM

    return arm

arm = kruskal(g)

# Función para guardar el Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, urlGuardado):
    with open(urlGuardado, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")

# Ruta para guardar el ARM
urlGuardado = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//PrimAlgoryth.txt'
guardar_grafo_archivo(arm, urlGuardado)
