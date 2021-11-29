# graph = [0, 1, 1, 1, 2, 2, 3, 3, 7, 8]
graph = [0, 0, 0]

ans = []
leaves = [vertex for vertex, _ in enumerate(graph)]
for vertex, parent in enumerate(graph):
    # Add strangers
    if vertex == parent and graph.count(vertex) == 1:
        ans.append(vertex)
    # Make leaves array
    if parent in leaves:
        leaves.remove(parent)

for val in leaves:
    if graph[val] not in ans:
        ans.append(graph[val])
print(ans)
