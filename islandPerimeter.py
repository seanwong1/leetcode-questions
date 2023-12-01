# Leetcode 463

from typing import List

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    perimeter = 0

    for row in range(len(grid)):
      for col in range(len(grid[row])):
        if grid[row][col]:
          if row - 1 < 0 or not grid[row - 1][col]:
            perimeter += 1
          if row + 1 >= len(grid) or not grid[row + 1][col]:
            perimeter += 1
          if col - 1 < 0 or not grid[row][col - 1]:
            perimeter += 1
          if col + 1 >=  len(grid[row]) or not grid[row][col + 1]:
            perimeter += 1

    return perimeter