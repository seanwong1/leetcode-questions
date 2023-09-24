# Leetcode 215

from typing import List

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    nums = sorted(nums)
    return nums[len(nums) - k]