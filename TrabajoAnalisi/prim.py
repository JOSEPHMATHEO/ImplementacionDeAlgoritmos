import networkx as nt
import matplotlib.pyplot as mt

def grafo_archivo(ruta_archivo):
    grafo = nt.Graph()
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            linea = linea.strip()
            parts = linea.split(',')
            u = parts[0]
            v = parts[1]
            weight = int(parts[2])
            grafo.add_edge(u, v, weight=weight)  # Añadir arista al grafo
    return grafo


# Ruta del archivo que contiene el grafo
urlLectura = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//Grafo50.txt'
g = grafo_archivo(urlLectura)


# Función para implementar el algoritmo de Prim
def prim(G):
    arm = nt.Graph()
    conjunto = set()

    # Selecciona el primer nodo como la raíz
    nodo_i = list(G.nodes())[0]
    conjunto.add(nodo_i)

    # Lista de las aristas conectadas al nodo inicial
    aristas = [(data['weight'], nodo_i, nodo_d) for nodo_d, data in G[nodo_i].items()]

    # Ordenación de las aristas en base al peso
    aristas.sort(key=lambda x: x[0])

    # Mientras el conjunto contenga aristas
    while aristas:
        weight, u, v = aristas.pop(0)  # Obtiene la arista de menor peso
        # Si el nodo 'v' no se encuentra en el conjunto:
        if v not in conjunto:
            conjunto.add(v)  # Se añade al conjunto
            arm.add_edge(u, v, weight=weight)  # Se añade al Árbol de Recubrimiento Mínimo

            # Añadir todas las aristas conectadas al nodo 'v' que no están en el conjunto
            for arista_v, peso in G[v].items():
                if arista_v not in conjunto:
                    aristas.append((peso['weight'], v, arista_v))

            # Ordenar las aristas por peso después de añadir nuevas aristas
            aristas.sort(key=lambda x: x[0])

    return arm

arm = prim(g)

# Función para guardar el Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, urlGuardado):
    with open(urlGuardado, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")


# Ruta para guardar el ARM
urlGuardado = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//PrimAlgoryth.txt'
guardar_grafo_archivo(arm, urlGuardado)
