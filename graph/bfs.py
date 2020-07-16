graph = {
        'a':['b','c'],
        'b':['d','e'],
        'c':['f'],
        'd':[],
        'e':['f'],
        'f':[]
        }

# edpresso bfs

queue = []
visited = {}

def bfs(visited, queue, node):
    visited[node] = True
    queue.append(node)

    while queue:
        s = queue.pop(0) # this is having O(n) complexity. Better to use deque.
        print(s, end=' ')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited[neighbour] = True
                queue.append(s)

bfs(visited, queue, 'a')
            
