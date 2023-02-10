import grafo_ponderado as GRP

# Grafo ejemplo con listas de adyacencia y pesos asociados
grafo = { '1': [(2, 1), (3, 2), (4, 3)],
          '2': [(1, 1), (3, 4)],
          '3': [(1, 2), (3, 4), (4, 5)],
          '4': [(1, 3), (3, 5)]}


def testGrafo():
    g = GRP.WeightedGraph(grafo)  # Crear el grafo con el diccionario de ejemplo

    print('Grafo')
    print(g)  # Visualizar el grafo
    print('Iteración')
    for n in g:  # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('3'))  # Arcos desde un nodo
    """
    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())  # Comprobar si grafo vacío
    print('Existe nodo A:', g.existNode('1'))  # Comprobar si existe nodo
    print('Existe nodo Z:', g.existNode('9'))
    print('Existe arco A-C:', g.existEdge([1, '3']))  # Comprobar arco
    print('Existe arco A-Z:', g.existEdge([1, '9']))

    print('\nAñadir nodos y arcos')
    g.addNode('5')  # Añadir nodo
    g.addEdge(('1', '5'), 6)  # Añadir arco con el peso
    g.addEdge(('2', '6'), 4)
    g.addEdge(('2', '7'), 5)
    print('Grafo resultante')
    print(g)

    print('Medidas')
    print('Grado de B:', g.degree('2'))  # Obtener grado de un nodo
    print('Grado de D:', g.degree('3'))
    print('Delta:', g.Delta())  # Obtener Delta del grafo
    print('Orden:', g.order())  # Obtener orden
    print('Tamaño:', g.size())  # Obtener tamaño

    print('\nRecorridos')
    print("DFS('A'):", g.DFS('1'))  # Recorrido DFS
    print("BFS('A'):", g.BFS('1'))  # Recorrido BFS

    # Obtener todos los caminos posibles entre dos nodos
    print(g.findPaths('1', '3'))"""
    # Obtener el camino más corto entre dos nodos
    path, weight = g.shortestPath(4, 6)
    print(f'Dijkstra: ruta D-G:{path} peso:{weight}')
    """
    print('\nEliminar arcos y nodos')
    g.removeEdge(['4', '1'])  # Eliminar arco
    g.removeNode('3')  # Eliminar nodo
    print('Grafo resultante')
    print(g)
    print('Nodos aislados:', g.isolatedNodes())  # Visualizar nodos aislados
"""

if __name__ == '__main__':
    testGrafo()