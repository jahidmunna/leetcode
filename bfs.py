from pprint import pprint
from typing import List, Tuple
from collections import defaultdict, deque

class BFS:
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

    def apply_bfs(self):
        first_node = self.edges[0][0]
        isVisited = []
        queue = deque()
        queue.append(first_node)
        
        while queue:
            node = queue.popleft()
            print(node)
            if not node in isVisited:
                isVisited.append(node)
                neighbour_nodes = self.graph[node]
                if neighbour_nodes and not neighbour_nodes in isVisited:
                    for neighbour in neighbour_nodes:
                        queue.append(neighbour)
        
               
                
            


edges = [
    (5, 3),
    (5, 7),
    (3, 2),
    (3, 4),
    (7, 8),
    (2,),
    (8,)
]

bfs = BFS(edges)
bfs.apply_bfs()