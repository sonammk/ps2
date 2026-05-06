import heapq


def dijkstra(graph, start):
    distances = {start: 0}
    queue = [(0, start)]

    while queue:
        current_distance, node = heapq.heappop(queue)
        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph.adjacency.get(node, []):
            distance = current_distance + weight
            if distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
