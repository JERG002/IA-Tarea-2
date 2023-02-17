# Grafo ponderado
# los arcos son bidireccionales, con peso único

import grafo as GR


class WeightedGraph(GR.Graph):
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de tuplas de la forma (nodo_destino, peso) 
    def __init__(self, graph={}):
        super().__init__(graph)


    # Devuelve el camino más corto entre dos nodos
    # camino más corto == el de menor peso
    # Algoritmo de Dijkstra para grafos ponderados

    def shortestPath(self, start, end):
        INF = float('inf')
        # Diccionario de nodos con un peso infinito
        unvisited = {node: INF for node in self.graph.keys()}
        # Diccionario de predecesores
        predecessor = {node: node for node in self.graph.keys()} 
        visited = {}
        current = start
        currentWeight = 0
        unvisited[current] = currentWeight      # nodo origen peso 0
        while True:
            for node, weight in self.graph[current]:
                if node not in unvisited:
                    continue                    # nodo ya tratado
                newWeight = currentWeight + weight
                if unvisited[node] > newWeight:
                    # Tomar el nodo con el menor peso
                    unvisited[node] = newWeight
                    predecessor[node] = current # predecesor con el menor peso
            visited[current] = currentWeight    # visitado con el menor peso 
            unvisited.pop(current)              # eliminar de los no visitados
            if not unvisited:
                break       # Terminar el bucle si no hay nodos por visitar
            # Tomar el nodo con el menor peso de los no visitados
            candidates = [(n, w) for n, w in unvisited.items() if w != INF]
            current, currentWeight = sorted(candidates, key = lambda x: x[1])[0]
        # Reconstrucción del camino de longitud mínima
        # Se parte del nodo final al inicial
        path = []
        node = end
        while True:
            path.append(node)
            if(node == predecessor[node]):
                break
            node = predecessor[node]
        # Devuelve una tupla con el camino y el peso total
        return (path[::-1], visited[end])