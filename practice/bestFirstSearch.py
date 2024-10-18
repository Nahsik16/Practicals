
from collections import defaultdict
import heapq

graph =defaultdict(list)
def add_edge(u,v,cost):
  graph[u].append((v,cost))

heuristic={
  0: 0,
  1: 1,
  2: 2,
  3: 1,
  4: 0

}
def greedy_bfs(source,goal):
  Priority_queue =[(heuristic[source],source)]
  visited =[False]*(len(graph)+1)

  while Priority_queue:
    _ , s =heapq.heappop(Priority_queue)
    
    print(s, end="->")
    if (s==goal):
      print("reached")
      return
    
    visited[s]=True

    for neighbor,_ in graph[s]:
      if not visited[neighbor]:
        heapq.heappush(Priority_queue, (heuristic[neighbor], neighbor))


add_edge(0, 1, 1)
add_edge(0, 3, 1)
add_edge(1, 2, 1)
add_edge(2, 3, 1)
add_edge(3, 4, 1)
add_edge(4, 2, 1)

greedy_bfs(0,4)


