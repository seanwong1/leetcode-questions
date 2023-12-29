# Leetcode 598

from typing import List

class Solution:
  def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    x = m
    y = n

    for op in ops:
      x = min(x, op[0])
      y = min(y, op[1])

    return x * y