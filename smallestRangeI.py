# Leetcode 906

from typing import List

class Solution:
  def smallestRangeI(self, nums: List[int], k: int) -> int:
    return max(0, abs(max(nums) - min(nums)) - 2 * k)