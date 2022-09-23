from pprint import pprint
from typing import List, Tuple
from collections import defaultdict, deque        

# apply recursively
def dfs(node, graph):
    print(node)
    neighbors = graph[node]
    if neighbors:
        for neighbor in neighbors:
            dfs(neighbor, graph)
    # else:
        # print(node)
        # return node
def apply_dfs(edges):
    graph = defaultdict(list)
    for pair in edges:
        try:
            u, v = pair
            graph[u].append(v)
        except:
            u  = list(pair)[0]
            graph[u]

    start = edges[0][0]
    for node, _ in graph.items():
        if node != start:
            graph[node] = graph[node][:1]
    
    dfs(node=start, graph=graph)


edges = [
    (5, 3),
    (5, 7),
    (3, 2),
    (3, 4),
    (7, 8),
    (2,),
    (8,)
]

# bfs = DFS(edges)
# bfs.apply_dfs()

apply_dfs(edges=edges)
