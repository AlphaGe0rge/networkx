import networkx as nx #Se usa para modelar la red de transporte como un grafo.
import matplotlib.pyplot as plt #Permite visualizar el grafo de estaciones.
import heapq #Se usa para manejar la cola de prioridad en el algoritmo de Dijkstra.

def dijkstra(graph, start, end):

    queue = [(0, start, [])]  # (Tiempo, estación actual, camino recorrido)
    visited = set()  # Creamos estructura de datos para las estaciones visitadas
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)  # Extraemos el nodo con menor tiempo
        
        if node in visited:
            continue  # Si ya visitamos la estación, la ignoramos
        
        path = path + [node]  # Agregamos la estación al camino recorrido
        
        if node == end:
            return cost, path  # Si llegamos a la estación destino, retornamos el resultado
        
        visited.add(node)  # Marcamos la estación como visitada
        
        for next_node, distance in graph[node].items():
            heapq.heappush(queue, (cost + distance, next_node, path))  # Agregamos las conexiones a la cola
    
    return float("inf"), []  # Si no hay camino, retornamos infinito y una lista vacía
