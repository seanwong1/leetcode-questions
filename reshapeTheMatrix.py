# Leetcode 566

from typing import List

class Solution:
  def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat) * len(mat[0]) != r * c:
      return mat
    else:
      result = []
      storage = []

      for row in mat:
        for num in row:
          storage.append(num)

      for row in range(r):
        result.append(storage[row * c:row * c + c])

    return result