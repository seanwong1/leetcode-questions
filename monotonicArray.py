# Leetcode 895

from typing import List

class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    decreasing = True
    increasing = True

    if len(nums) == 1:
      return True

    for i in range(len(nums) - 1):
      if not nums[i] <= nums[i + 1]:
        increasing = False
        break

    for i in range(len(nums) - 1):
      if not nums[i] >= nums[i + 1]:
        decreasing = False
        break

    return decreasing or increasing