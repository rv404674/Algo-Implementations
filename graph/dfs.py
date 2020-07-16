# NOTE
# TIme complexity of In
# for list - Average(O(n)) ( Implemented as sequences)
# for dict - Average O(1), Worst O(n) ( as dict is hashing data type)
# edpresso.com for dfs implementation


# for a directed graph, the sum of size of adjaceny list of all nodes is E. 2+2+1+1 = 6
# hence O(V) + O(E) = O(V+E)
# OV) because you nead to visit each vertex alteast once.
# O(E) because you need to go through outgoing paths (edges) for each node
# for densely populated graphs, e=v^2. hence O(v^2)
graph = {
        'a':['b','c'],
        'b':['d','e'],
        'c':['f'],
        'd':[],
        'e':['f'],
        'f':[]
        }

# visited = {}

# def dfs(graph, visited, node):
#     if node not in visited:
#         print(node)
#         visited[node] = True
#         for neighbour in graph[node]:
#             dfs(graph, visited, neighbour)

#OR
def dfs(graph, visited, node):
    print(node)
    visited[node] = True
    print(visited, "VISITED")
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, visited, neighbour)

def dfsutil():
    visited = {}
    dfs(graph, visited, 'a')


dfsutil()