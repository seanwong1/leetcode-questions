# Leetcode 1351

from typing import List

class Solution:
  def countNegatives(self, grid: List[List[int]]) -> int:
    result = 0
    row = 0
    col = 1

    while row < len(grid):
      while col < len(grid[row]) + 1 and grid[row][-col] < 0:
        result += len(grid) - row
        col += 1
      row += 1

    return result