# Leetcode 645

from typing import List

class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    total = sum(range(1, len(nums) + 1))
    missing = total - sum(set(nums))
    repeated = sum(nums) + missing - total
    return [repeated, missing]