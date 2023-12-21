def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


predefined_graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

start_node = 0
visited_nodes = set()

print("DFS traversal starting from node", start_node)
dfs(predefined_graph, start_node, visited_nodes)
