# Leetcode 1475

from typing import List

class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    result = [None] * len(prices)
    discounts = []

    for i in range(len(prices) - 1, -1, -1):
      while discounts:
        if prices[i] >= discounts[-1]:
          result[i] = prices[i] - discounts[-1]
          break
        else:
          discounts.pop()

      if not discounts:
        result[i] = prices[i]

      discounts.append(prices[i])

    return result