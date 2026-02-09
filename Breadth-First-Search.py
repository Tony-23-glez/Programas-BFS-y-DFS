# Breadth-First Search (BFS) es búsqueda en anchura, implementado con Python
# Creacion del grafo 
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'], 
    'D': [],
    'E': []
}


# implemtacion de BFS
def bfs(grafo, inicio):
    visitados = []
    cola = []

    visitados.append(inicio)
    cola.append(inicio)

    while cola: 
        nodo = cola.pop(0)
        print(nodo)

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

# Ejecucion de BFS
bfs(grafo, 'A')