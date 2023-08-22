# Leetcode 133

class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node: 'Node') -> 'Node':
    storage = {}
    if not node:
      return None

    def helper(node):
      if node in storage:
        return storage[node]
      else:
        storage[node] = Node(node.val)
        for neighbor in node.neighbors:
          newNeighbor = helper(neighbor)
          storage[node].neighbors.append(newNeighbor)
      return storage[node]

    return helper(node)