import sys

def prim(graph):
    num_nodes = len(graph)
    key = [sys.maxsize] * num_nodes
    parent = [None] * num_nodes
    visited = [False] * num_nodes

    
    key[0] = 0
    parent[0] = -1

    for _ in range(num_nodes):
        
        min_key = sys.maxsize
        min_index = -1
        for i in range(num_nodes):
            if not visited[i] and key[i] < min_key:
                min_key = key[i]
                min_index = i

        
        visited[min_index] = True

        
        for j in range(num_nodes):
            if graph[min_index][j] > 0 and not visited[j] and graph[min_index][j] < key[j]:
                key[j] = graph[min_index][j]
                parent[j] = min_index

    return parent, key


example_graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

result_parent, result_key = prim(example_graph)


print("Edges in the Minimum Spanning Tree:")
for i in range(1, len(result_parent)):
    print(f"Edge {result_parent[i]} - {i}, Weight: {example_graph[i][result_parent[i]]}")
