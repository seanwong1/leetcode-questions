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
        if target < nums[left]:
          return left
        elif target > nums[right]:
          return right + 1
        else:
          midpoint = (left + right) // 2
          if target < nums[midpoint]:
            right = midpoint - 1
          else:
            left = midpoint + 1