import collections

graph = {
    'A':['B', 'C'],
    'B':['D', 'E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

# NOTE
# 'in' in set is O(1)
# also popleft() of dequeu is O(1), and pop() of dequeue is (popright)
def bfs(graph, root):
    visited, queue = set(), collections.deque( [root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(vertex,visited)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
                visited.add(i)    

bfs(graph, 'A')