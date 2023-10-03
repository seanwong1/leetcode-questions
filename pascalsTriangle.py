# Leetcode 118

from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1:
      return [[1]]
    else:
      result = self.generate(numRows - 1)
      newRow = [1] * numRows

      for i in range(1, numRows - 1):
        newRow[i] = result[-1][i - 1] + result[-1][i]

    result.append(newRow)
    return result