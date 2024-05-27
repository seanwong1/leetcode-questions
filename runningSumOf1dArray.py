# Leetcode 1480

from typing import List

class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    cumulative = 0
    result = []

    for num in nums:
      cumulative += num
      result.append(cumulative)

    return result