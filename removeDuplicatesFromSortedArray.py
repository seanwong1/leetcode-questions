# Leetcode 26

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    left = 1

    for right in range(left, len(nums)):
      if not nums[right] == nums[right - 1]:
        nums[left] = nums[right]
        left += 1

    return left