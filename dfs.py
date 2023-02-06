from pprint import pprint
from typing import List, Tuple
from collections import defaultdict, deque

class DFS:
    def __init__(self, edges: List[Tuple]) -> None:
        self.edges = edges 
        self.graph = self.build_graph()
        
        print()

    def build_graph(self) -> defaultdict:
        graph = defaultdict(list)
        for pair in self.edges:
            try:
                u, v = pair
                graph[u].append(v)
            except:
                u  = list(pair)[0]
                graph[u]
        return graph

    def apply_dfs(self):
        first_node = self.edges[0][0]
        isVisited = []
        stack = []
        stack.append(first_node)
        
        while stack:
            node = stack.pop()
            print(node)
            if not node in isVisited:
                isVisited.append(node)
                neighbour_nodes = self.graph[node]
                if neighbour_nodes:
                    for neighbour in neighbour_nodes:
                        stack.append(neighbour)
        
               
                
# apply recursively
def dfs(visited, node, graph):
    if not node in visited:
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, neighbor, graph)

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
    dfs(visited=[], node=start, graph=graph)


# edges = [
#     (5, 3),
#     (5, 7),
#     (3, 2),
#     (3, 4),
#     (7, 8),
#     (2,),
#     (8,)
# ]

#      1
#    / \
#   2   3
#  / \
# 4   5

edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5)
]

# bfs = DFS(edges)
# bfs.apply_dfs()

apply_dfs(edges=edges)
