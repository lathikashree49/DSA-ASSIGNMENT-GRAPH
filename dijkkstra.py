import heapq

def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


small_graph = [
    [0, 2, 4, 0],
    [0, 0, 1, 4],
    [0, 0, 0, 2],
    [0, 0, 0, 0]
]

start_node = 0
result = dijkstra(small_graph, start_node)

for i, distance in enumerate(result):
    print(f"Distance from node {start_node} to node {i}: {distance}")
