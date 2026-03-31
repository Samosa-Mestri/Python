#A*


graphNodes={
    'S':[('A',2),('B',5)],
    'A':[('C',4),('D',2)],
    'B':[('D',6),('E',3)],
    'C':[('G',7)],
    'D':[('G',1)],
    'E':[('G',5)],
    'G': None
}

def getNeighbours(node):
  return graphNodes.get(node,[])

def hue(node):
  heuristicValue = {
      'S':10,
      'A':4,
      'B':8,
      'C':3,
      'D':6,
      'E':5,
      'G':0
  }
  return heuristicValue.get(node,float('inf'))

def ast(start,goal):
  openSet = set([start])
  closedSet = set()
  cost = {}
  parent = {}

  cost[start] = 0
  parent[start] = start

  while openSet:
    currentNode = None

    for node in openSet:
      if currentNode == None or cost[node] +hue(node) < cost[currentNode] + hue(currentNode):
        currentNode = node
    if currentNode is None:
      print("Path not found")
      return None
    if currentNode == goal:
      path =[]
      while currentNode != start:
        path.append(currentNode)
        currentNode = parent[currentNode]
      path.append(start)
      path.reverse()
      print("Path found", path)
      return path

    for (neighbour,weight) in getNeighbours(currentNode):
      newCost = cost[currentNode] + weight
      if neighbour not in openSet and neighbour not in closedSet:
        openSet.add(neighbour)
        parent[neighbour] = currentNode
        cost[neighbour] = newCost
      else:
        if newCost < cost[neighbour]:
          cost[neighbour] = newCost
          parent[neighbour] = currentNode
          if neighbour in closedSet:
            closedSet.remove(neighbour)
            openSet.add(neighbour)


    openSet.remove(currentNode)
    closedSet.add(currentNode)
  print("Path not found")
  return None

ast('S','G')
