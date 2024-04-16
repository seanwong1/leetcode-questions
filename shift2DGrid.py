# Leetcode 1260

from typing import List
from itertools import chain

class Solution:
  def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    result = []
    storage = list(chain.from_iterable(grid))
    flattened = storage[-(k % (m * n)):] + storage[:-(k % (m * n))]

    for i in range(m):
      row = []
      for j in range(n):
        row.append(flattened[n * i + j])
      result.append(row)

    return result