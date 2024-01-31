# Leetcode 766

from typing import List

class Solution:
  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    for row in range(0, len(matrix) - 1):
      nextRow = matrix[row + 1]
      for col in range(0, len(matrix[row]) - 1):
        if matrix[row][col] != nextRow[col + 1]:
          return False

    return True