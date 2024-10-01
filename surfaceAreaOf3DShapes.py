# Leetcode 892

from typing import List

class Solution:
  def surfaceArea(self, grid: List[List[int]]) -> int:
    surface_area = 0
    ROW = len(grid)
    COL = len(grid[0])

    for i in range(ROW):
      for j in range(COL):
        if grid[i][j] > 0:
          surface_area += 2

          if i - 1 >= 0:
            surface_area += max(grid[i][j] - grid[i - 1][j], 0)
          else:
            surface_area += grid[i][j]

          if i + 1 < ROW:
            surface_area += max(grid[i][j] - grid[i + 1][j], 0)
          else:
            surface_area += grid[i][j]

          if j - 1 >= 0:
            surface_area += max(grid[i][j] - grid[i][j - 1], 0)
          else:
            surface_area += grid[i][j]

          if j + 1 < COL:
            surface_area += max(grid[i][j] - grid[i][j + 1], 0)
          else:
            surface_area += grid[i][j]

    return surface_area