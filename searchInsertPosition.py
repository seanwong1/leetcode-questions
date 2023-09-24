# Leetcode 35

from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    try:
      return nums.index(target)
    except ValueError:
      left = 0
      right = len(nums) - 1
      while left <= right:
        midpoint = (left + right) // 2
        if target < nums[midpoint]:
          right = midpoint - 1
        elif target > nums[midpoint]:
          left = midpoint + 1
        else:
          return midpoint
      return right + 1