# Leetcode 199

from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    row = [1]

    for i in range(rowIndex):
      temp = [1] * (len(row) + 1)
      for j in range(1, len(temp) - 1):
        temp[j] = row[j - 1] + row[j]
      row = temp

    return row