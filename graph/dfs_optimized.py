# link - https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[]
}

def dfsutil(graph, visited, node):
    print(node)
    print(visited)
    visited.add(node)

    for i in graph[node]:
        if i not in visited:
            dfsutil(graph, visited,i)


def dfs():
    # NOTE - in operation in set and dict is O(1)
    visited = set()
    # NOTE - start dfs from every edge, as there might be a disconnected node
    for node in graph.keys():
        dfsutil(graph, visited, node)

dfs()
