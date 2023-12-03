# Leetcode 485

from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    result = 0
    counter = 0

    for bit in nums:
      if not bit:
        counter = 0
      else:
        counter += 1
        if counter > result:
          result = counter

    return result