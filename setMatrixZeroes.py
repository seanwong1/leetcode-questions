# Leetcode 73

from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    storage = {}
    for i in range(HEIGHT):
      for j in range(WIDTH):
        if matrix[i][j] == 0:
          if not i in storage:
            storage[i] = [j]
          else:
            storage[i].append(j)

    for row in storage:
      matrix[row] = [0] * WIDTH
      for column in storage[row]:
        for i in range(HEIGHT):
          matrix[i][column] = 0