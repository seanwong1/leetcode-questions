# Leetcode 1030

from typing import List

class Solution:
  def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    storage = {}

    for row in range(rows):
      for col in range(cols):
        storage[row, col] = abs(rCenter - row) + abs(cCenter - col)

    return [list(x) for x in sorted(storage, key=storage.get)]