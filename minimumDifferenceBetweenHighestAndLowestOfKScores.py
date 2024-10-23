# Leetcode 1984

from typing import List

class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
    nums.sort()

    diff = max(nums) - min(nums)
    for i in range(len(nums) - k + 1):
      diff = min(diff, abs(nums[i + k - 1] - nums[i]))

    return diff