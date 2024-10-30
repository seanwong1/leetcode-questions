# Leetcode 2016

from typing import List

class Solution:
  def maximumDifference(self, nums: List[int]) -> int:
    minimum = max(nums) + 1
    diff = -1

    for num in nums:
      if num < minimum:
        minimum = num
      else:
        diff = max(diff, num - minimum)

    return diff