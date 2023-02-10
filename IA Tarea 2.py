import random
import grafo_ponderado as GRP
import grafo_ponderado2 as Prueba



def generador_grafo(nodos):
    instancia = {}
    for i in range(1,nodos+1):
        nodos_adyacentes = random.randint(1, nodos-1)
        lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        while(i in lista_nodos_adyacentes):
            nodos_adyacentes = random.randint(1,nodos-1)
            lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        
        lista_tuplas = []
        for j in range(0, len(lista_nodos_adyacentes)):
            lista_tuplas.append(((lista_nodos_adyacentes[j]),random.randint(1,1000)))
        instancia[i] = lista_tuplas
    return instancia
g = generador_grafo(50)
grafo = GRP.WeightedGraph(g)
while(len(grafo.isolatedNodes())>0):
    g = generador_grafo(50)
    grafo = GRP.WeightedGraph(g)
print(g)
path, weight = grafo.shortestPath(1, 50)
print(f'Dijkstra: ruta D-G:{path} peso:{weight}')