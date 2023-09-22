# Leetcode 26

from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    k, left, right = 1, 0, 1

    while right < len(nums):
      if not nums[left] == nums[right]:
        left += 1
        [nums[left], nums[right]] = [nums[right], nums[left]]
        k += 1
      right += 1

    return k