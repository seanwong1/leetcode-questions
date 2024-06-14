# Leetcode 1582

from typing import List

class Solution:
  def numSpecial(self, mat: List[List[int]]) -> int:
    result = 0
    rows = [0] * len(mat)
    cols = [0] * len(mat[0])

    for i in range(len(rows)):
      for j in range(len(cols)):
        if mat[i][j] == 1:
          rows[i] += 1
          cols[j] += 1

    for i in range(len(rows)):
      for j in range(len(cols)):
        if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
          result += 1

    return result