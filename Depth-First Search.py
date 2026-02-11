#Depth-First Search (DFS) es búsqueda en profundidad, implementado con Python
# creacion del grafo
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'F': ['J'],
    'E': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

# implementacion de DFS
def dfs(grafo, nodo, visitados):
    visitados.add(nodo)
    print(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Ejecucion de DFS
visitados = set()
dfs(grafo, 'A', visitados)