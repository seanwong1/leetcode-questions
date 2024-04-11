# Leetcode 1217

from typing import List
from collections import Counter

class Solution:
  def minCostToMoveChips(self, position: List[int]) -> int:
    coins = Counter(position)
    result = {}
    evens = 0
    odds = 0

    for key, value in coins.items():
      if key % 2 == 0:
        evens += value
      else:
        odds += value

    for key, value in coins.items():
      result[key] = 0
      if key % 2 == 0:
        result[key] += odds
      else:
        result[key] += evens

    return min(result.values())