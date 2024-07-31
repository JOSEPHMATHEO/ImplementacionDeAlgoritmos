import networkx as nt
import matplotlib.pyplot as mt

def grafo_archivo(ruta_archivo):
    grafo = nt.DiGraph()
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            linea = linea.strip()  # Eliminar espacios en blanco
            parts = linea.split(',')  # Separar los atributos por ','
            u = int(parts[0])
            v = int(parts[1])
            weight = int(parts[2])
            grafo.add_edge(u, v, weight=weight)  # Añadir arista al grafo
    return grafo


# Ruta del archivo que contiene el grafo
ruta = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//Grafo30.txt'
g = grafo_archivo(ruta)


# Función para implementar el algoritmo de Dijkstra
def dijkstra(G, origen):
    distancias = {n: float('infinity') for n in G.nodes()}  # Inicializar distancias
    distancias[origen] = 0  # La distancia desde el origen a sí mismo es 0
    parents = {n: None for n in G.nodes()}  # Inicializar padres

    lista_prioridades = [(0, origen)]

    while lista_prioridades:
        d_actual, n_actual = min(lista_prioridades, key=lambda x: x[0])
        lista_prioridades.remove((d_actual, n_actual))

        # Relajar aristas
        for adya, peso in G[n_actual].items():
            weight = peso['weight']
            distancia = d_actual + weight

            if distancia < distancias[adya]:
                distancias[adya] = distancia
                parents[adya] = n_actual
                lista_prioridades.append((distancia, adya))

    return distancias, parents


# Función para construir el Árbol de Recubrimiento Mínimo (ARM) a partir de los padres
def arbol_recubrimiento_min(G, parents, origen):
    arm = nt.DiGraph()

    for node in G.nodes():
        if parents[node] is not None:
            arm.add_edge(parents[node], node, weight=G[parents[node]][node]['weight'])

    return arm


# Ejecutar el algoritmo de Dijkstra
origen = list(g.nodes)[0]
distancias, parents = dijkstra(g, origen)

# Construir el Árbol de Recubrimiento Mínimo
arm = arbol_recubrimiento_min(g, parents, origen)


# Función para guardar el Árbol de Recubrimiento Mínimo en un archivo
def guardar_grafo_archivo(arm, urlGuardado):
    with open(urlGuardado, 'w') as archivo:
        for (u, v, p) in arm.edges.data('weight'):
            archivo.write(f"{u},{v},{p}\n")


# Ruta para guardar el ARM
urlGuardado = 'C://Users//sucol//OneDrive//Escritorio//Nueva carpeta (2)//PrimAlgoryth.txt'
guardar_grafo_archivo(arm, urlGuardado)
