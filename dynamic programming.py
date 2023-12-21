import sys

def floyd_warshall(graph):
    num_nodes = len(graph)

    
    distance_matrix = [row[:] for row in graph]

    
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

    return distance_matrix

small_graph = [
    [0, 2, sys.maxsize, 5],
    [sys.maxsize, 0, 1, 4],
    [sys.maxsize, sys.maxsize, 0, 2],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

result = floyd_warshall(small_graph)


print("Shortest distances between nodes:")
for row in result:
    print(row)
