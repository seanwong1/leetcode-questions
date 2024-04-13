# Leetcode 1217

from typing import List
from collections import Counter

class Solution:
  def minCostToMoveChips(self, position: List[int]) -> int:
    evens = 0
    odds = 0

    for coin in position:
      if coin % 2 == 0:
        evens += 1
      else:
        odds += 1

    return min(evens, odds)