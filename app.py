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
def plot_graph(graph, shortest_path):
    G = nx.Graph()  # Creamos un grafo vacío
    
    # Agregamos nodos y conexiones al grafo
    for station, connections in graph.items():
        for connected_station, distance in connections.items():
            G.add_edge(station, connected_station, weight=distance)
    
    pos = nx.spring_layout(G, seed=42)  # Posiciónamos los nodos
    plt.figure(figsize=(10, 6))  # Le damos tamaño del gráfico
    
    edges = G.edges(data=True)  # Obtenemos las conexiones del grafo
    
    # Resaltamos la ruta más corta en rojo
    edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) or (v, u) in zip(shortest_path, shortest_path[1:]) else 'black' for u, v, _ in edges]
    
    # Dibujamos el grafo
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", edge_color=edge_colors, font_size=10, font_weight="bold")
    
    # Etiquetamos los tiempos de viaje
    edge_labels = {(u, v): d['weight'] for u, v, d in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Mapa del Metro de Bogotá con Ruta Óptima en Rojo")
    plt.show()