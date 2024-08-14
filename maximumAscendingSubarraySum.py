# Leetcode 1800

from typing import List

class Solution:
  def maxAscendingSum(self, nums: List[int]) -> int:
    current = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):
      if nums[i] <= nums[i - 1]:
        current = 0
      current += nums[i]
      maximum = max(maximum, current)

    return maximum