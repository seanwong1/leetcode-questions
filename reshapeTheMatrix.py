# Leetcode 566

from typing import List

class Solution:
  def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat) * len(mat[0]) != r * c:
      return mat
    else:
      result = [[None for col in range(c)] for row in range(r)]
      current = 0

      for row in range(r):
        for col in range(c):
          result[row][col] = mat[current // len(mat[0])][current % len(mat[0])]
          current += 1

    return result