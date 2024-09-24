# Leetcode 1886

from typing import List

class Solution:
  def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    for i in range(4):
      if self.checkMatrices(mat, target):
        return True

      self.rotateMatrix(mat)

    return False

  def checkMatrices(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if matrix[i][j] != target[j][len(matrix) - i - 1]:
          return False

    return True

  def rotateMatrix(self, matrix: List[List[int]]) -> None:
    for layer in range(len(matrix) // 2):
      start = layer
      end = len(matrix) - 1 - layer

      for i in range(start, end):
        offset = i - start
        top = matrix[start][i]
        matrix[start][i] = matrix[end - offset][start]
        matrix[end - offset][start] = matrix[end][end - offset]
        matrix[end][end - offset] = matrix[i][end]
        matrix[i][end] = top