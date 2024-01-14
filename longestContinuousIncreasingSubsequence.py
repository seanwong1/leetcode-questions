# Leetcode 674

from typing import List

class Solution:
  def findLengthOfLCIS(self, nums: List[int]) -> int:
    result = 1
    left = 0
    right = 1

    while left <= right and right < len(nums):
      if nums[right] > nums[right - 1]:
        right += 1
        result = max(result, right - left)
      else:
        left = right
        right = left + 1

    return result