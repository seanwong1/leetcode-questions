# Leetcode 1971

from typing import List
from collections import defaultdict

class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

    def helper(node, visited):
      if node == destination:
        return True

      visited.add(node)
      for neighbor in graph[node]:
        if not neighbor in visited:
          if helper(neighbor, visited):
            return True

      return False

    visited = set()
    return helper(source, visited)