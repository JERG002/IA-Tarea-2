import grafo as GR

# Grafo ejemplo con listas de adyacencia
grafo = {'A': ['B', 'C', 'D'],
         'B': ['A', 'C'],
         'C': ['A', 'B', 'D'],
         'D': ['A', 'C']}


def testGrafo():
    g = GR.Graph(grafo)  # Crear el grafo con el diccionario de ejemplo

    print('Grafo')
    print(g)  # Visualizar el grafo
    print('Iteración')
    for n in g:  # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos
    print('Arcos:', g.edges())  # Visualizar todos los arcos
    print('Arcos desde el nodo C:', g.edges('C'))  # Arcos desde un nodo

    print('\nComprobaciones')
    print('Vacío:', g.isEmpty())  # Comprobar si grafo vacío
    print('Existe nodo A:', g.existNode('A'))  # Comprobar si existe nodo
    print('Existe nodo Z:', g.existNode('Z'))
    print('Existe arco A-C:', g.existEdge(['A', 'C']))  # Comprobar arco
    print('Existe arco A-Z:', g.existEdge(['A', 'Z']))

    print('\nAñadir nodos y arcos')
    g.addNode('E')  # Añadir nodo
    g.addEdge(['E', 'A'])  # Añadir arco
    g.addNode('F')
    g.addEdge(['F', 'F'])
    g.addEdge(['A', 'B'])
    g.addEdge(['G', 'B'])
    g.addEdge(['B', 'B'])
    g.addEdge(('B', 'F'))
    print('Grafo resultante')
    print(g)

    print('Medidas')
    print('Grado de B:', g.degree('B'))  # Obtener grado de un nodo
    print('Grado de D:', g.degree('D'))
    print('Delta:', g.Delta())  # Obtener Delta del grafo
    print('Orden:', g.order())  # Obtener orden
    print('Tamaño:', g.size())  # Obtener tamaño

    print('\nRecorridos')
    print("DFS('A'):", g.DFS('A'))  # Recorrido DFS
    print("BFS('A'):", g.BFS('A'))  # Recorrido BFS

    # Obtener todos los caminos posibles entre dos nodos
    print('Caminos de A a C:', g.findPaths('A', 'C'))
    # Obtener el camino más corto entre dos nodos
    print('Más corto de A a C:', g.shortestPath('A', 'C'))

    print('\nEliminar arcos y nodos')
    g.removeEdge(['B', 'B'])  # Eliminar arco
    g.removeNode('B')  # Eliminar nodo
    g.removeEdge(['G', 'A'])
    g.removeNode('Z')  # Eliminar nodo inexistente
    g.removeEdge(['B', 'Z'])  # Eliminar arco inexistente
    print('Grafo resultante')
    print(g)
    print('Nodos aislados:', g.isolatedNodes())  # Visualizar nodos aislados


if __name__ == '__main__':
    testGrafo()