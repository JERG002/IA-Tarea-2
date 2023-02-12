import random
import grafo_ponderado as GRP




def generador_grafo(nodos):
    #indice_nodo = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','AA'}
    instancia = {}
    for i in range(1,nodos+1):
        nodos_adyacentes = random.randint(1, nodos-1)
        lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        while(i in lista_nodos_adyacentes):
            nodos_adyacentes = random.randint(1,nodos-1)
            lista_nodos_adyacentes = random.sample(range(1,nodos), nodos_adyacentes)
        
        lista_tuplas = []
        for j in range(0, len(lista_nodos_adyacentes)):
            lista_tuplas.append((str(lista_nodos_adyacentes[j]),random.randint(1,1000)))
        instancia[str(i)] = lista_tuplas

    return instancia

nodo = {'1','2','3'}

grafo = generador_grafo(3)
print(grafo)
for i in nodo:
    for j in grafo[i]:
        n1, n2 = tuple(j)
        n = (n1,n2)
        for let in nodo:
            if i != let:
                if n in grafo[let]:
                    
                    if not((let, n2) in grafo[n1]):
                        
                        grafo[n1].insert(0,(let, n2))
print(grafo)
print("AQUI ES EL GRAFO QUE SIGUE")

g = GRP.WeightedGraph(grafo)
"""while(len(grafo.isolatedNodes())>0):
    grafo = generador_grafo(3)
    g = GRP.WeightedGraph(grafo)"""
print(grafo)
"""path, weight = grafo.shortestPath('A', 'AA')
print(f'Dijkstra: ruta D-G:{path} peso:{weight}')"""