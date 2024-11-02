# Leetcode 1431

from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    mostCandy = max(candies)
    result = [None] * len(candies)

    for kid in range(len(candies)):
      result[kid] = candies[kid] + extraCandies >= mostCandy

    return result