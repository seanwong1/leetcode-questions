# Leetcode 1380

from typing import List

class Solution:
  def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    mins = set([min(row) for row in matrix])
    maxs = set([max(col) for col in zip(*matrix)])

    return list(mins & maxs)