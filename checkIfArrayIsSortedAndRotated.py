# Leetcode 1752

from typing import List

class Solution:
  def check(self, nums: List[int]) -> bool:
    start = nums[::-1].index(min(nums))
    minCount = nums.count(min(nums))
    counter = 0

    while counter < len(nums) - 1 - minCount:
      current = (start + counter) % len(nums)
      next = (current + 1) % len(nums)
      if nums[current] <= nums[next]:
        counter += 1
      else:
        return False

    return True