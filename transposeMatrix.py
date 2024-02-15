# Leetcode 867

from typing import List

class Solution:
  def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    COLS = len(matrix[0])
    ROWS = len(matrix)
    result = [[None for row in range(ROWS)] for col in range((COLS))]

    for i in range(ROWS):
      for j in range(COLS):
        result[j][i] =  matrix[i][j]

    return result