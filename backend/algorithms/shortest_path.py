from algorithms.dijkstra import dijkstra


def shortest_path_distance(graph, start, end):
    distances = dijkstra(graph, start)
    return distances.get(end)
