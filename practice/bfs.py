
from collections import defaultdict

graph = defaultdict(list)

def add_edge(u, v):
    graph[u].append(v)

def bfs(source):
    # Initialize visited list based on the number of vertices in the graph
    visited = [False] * (len(graph) + 1)

    # Use a queue to manage the BFS
    queue = [source]
    visited[source] = True

    while queue:
        s = queue.pop(0)  # Dequeue the first element
        print(s, end=" -> ")

        # Enqueue all unvisited neighbors
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# Adding edges to the graph
add_edge(0, 1)
add_edge(0, 3)
add_edge(1, 2)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 2)

print("Starting BFS")
bfs(0)
