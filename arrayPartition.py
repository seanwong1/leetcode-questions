# Leetcode 561

from typing import List

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    result = 0
    nums = sorted(nums)

    for i in range(0, len(nums), 2):
      result += min(nums[i], nums[i + 1])

    return result