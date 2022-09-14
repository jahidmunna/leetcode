# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def isCyclicUtil(size, visited, recStack, graph):
    visited[size] = True
    recStack[size] = True

    for neighbour in graph[size]:
        if visited[neighbour] == False:
            if isCyclicUtil(neighbour, visited, recStack, graph) == True:
                return True
        elif recStack[neighbour] == True:
            return True
    recStack[size] = False
    return False
    
def solution(size, edges):
    """
    Solution description.

    Time Complexity: ...
    Space Complexity: ...
    """
    graph = defaultdict(list)
    
    # add edges
    for i in range(0, len(edges), 2):
        v1, v2 = edges[i], edges[i+1]
        graph[v1].append(v2)

    # check if cyclic
    visited = [False] * (size + 1)
    recStack = [False] * (size + 1)
    for node in range(size):
        if visited[node] == False:
            if isCyclicUtil(node,visited,recStack, graph) == True:
                return True
    return False

print(solution(4,[0,1,1,2,2,3,3,0]))
print(solution(3,[0,1,1,2,2,0]))

