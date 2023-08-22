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

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

s = Solution()

print(s.cloneGraph(node1))