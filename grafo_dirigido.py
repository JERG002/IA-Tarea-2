# Grafo dirigido

import grafo as GR

class DirectedGraph(GR.Graph):
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de los nodos siguientes al nodo
    def __init__(self, graph={}):
        super().__init__(graph)

    # Elimina un nodo del grafo
    # Elimina todos los arcos desde otros nodos
    def removeNode(self, node):
        if node in self.graph:
            nodes = list(self.graph)
            for n in nodes:
                if node in self.graph[n]:
                    self.graph[n].remove(node)
            self.graph.pop(node)

    # Inserta una arco entre los nodos indicados
    # La arco es una lista con el nodo origen y destino
    # Si no existe alguno de los nodos lo inserta
    def addEdge(self, edge):
        start, end = tuple(edge)
        if end not in self.graph:
            self.graph[end] = []            # no existe nodo destino, se crea
        if start in self.graph:
            if end not in self.graph[start]:
                self.graph[start].append(end)
        else:
            self.graph[start] = [end]       # no existe nodo origen, se crea

    # Elimina un arco entre nodos
    # El arco es una lista con los nodos que une
    def removeEdge(self, edge):
        start, end = tuple(edge)
        if start in self.graph:
            if end in self.graph[start]:
                self.graph[start].remove(end)

    # Devuelve una lista de los nodos aislados
    def isolatedNodes(self):
        return [n for n, e in self.graph.items() if self.inDegree(n) == 0]

    # Semigrado exterior
    def outDegree(self, node):
        return len(self.graph[node])

    # Semigrado interior
    def inDegree(self, node):
        return len([n for n, e in self.graph.items() if node != n and node in e])