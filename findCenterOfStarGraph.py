# Leetcode 1791

from typing import List

class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    star = {}

    for edge in edges:
      u, v = edge
      if u in star:
        star[u] += 1
      else:
        star[u] = 1
      if v in star:
        star[v] += 1
      else:
        star[v] = 1

    return max(star, key=star.get)