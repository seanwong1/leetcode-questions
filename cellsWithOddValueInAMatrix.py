# Leetcode 1252

from typing import List

class Solution:
  def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
    # counts = [[0 for col in range(n)] for row in range(m)]
    # result = 0

    # for row, col in indices:
    #   for i in range(n):
    #     counts[row][i] += 1
    #   for j in range(m):
    #     counts[j][col] += 1

    # for row in counts:
    #   for count in row:
    #     if count % 2 == 1:
    #       result += 1

    # return result

    rowTotals = [0 for row in range(m)]
    colTotals = [0 for col in range(n)]
    result = 0

    for row, col in indices:
      rowTotals[row] += 1
      colTotals[col] += 1

    numOdds = 0
    for row in rowTotals:
      if row % 2 == 1:
        numOdds += 1

    for col in colTotals:
      if col % 2 == 0:
        result += numOdds
      else:
        result += m - numOdds

    return result