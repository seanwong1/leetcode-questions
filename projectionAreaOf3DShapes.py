# Leetcode 883

from typing import List

class Solution:
  def projectionArea(self, grid: List[List[int]]) -> int:
    area1 = len(grid) * len(grid[0])
    area2 = 0
    area3 = 0

    for row in grid:
      for cell in row:
        if cell == 0:
          area1 -= 1

    for row in grid:
      area2 += max(row)

    for col in zip(*grid):
      area3 += max(col)

    return area1 + area2 + area3