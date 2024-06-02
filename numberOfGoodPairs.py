# Leetcode 1512

from typing import List

class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    result = 0
    storage = {}

    for num in nums:
      if num in storage:
        storage[num] += 1
        result += storage[num]
      else:
        storage[num] = 0

    return result