# Leetcodee 1572

from typing import List

class Solution:
  def diagonalSum(self, mat: List[List[int]]) -> int:
    result = 0
    matLen = len(mat)

    middle = mat[matLen // 2][matLen // 2] if matLen % 2 == 1 else 0

    for i in range(matLen):
      result += mat[i][i]
      result += mat[matLen - 1 - i][i]

    return result - middle