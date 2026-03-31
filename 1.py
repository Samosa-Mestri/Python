import collections
graph={
    0:[1,3],1:[0,2,4],2:[1,5],3:[0,6],4:[1,5,7],5:[2,4,8],6:[3],7:[4,8],8:[5,7]
}

def bfs(graph,start):
  visited = set()
  queue = collections.deque([start])
  visited.add(start)

  while queue:
    vertex = queue.popleft()
    print(str(vertex)+"",end=' ')

    for neighbours in graph[vertex]:
      if neighbours not in visited:
        visited.add(neighbours)
        queue.append(neighbours)
print("Breadth First Traversal")
bfs(graph,0)


def dfs(graph,start,visited=None):
  if visited == None:
    visited = set()

  visited.add(start)
  print(start)

  for neighbours in graph[start]:
    if neighbours not in visited:
      dfs(graph,neighbours,visited)
  return visited

print("\nDepth First Traversal")
dfs(graph,0)
