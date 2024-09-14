# Leetcode 1863

from typing import List

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    def helper(index, total):
      if index == len(nums):
        return total
      else:
        include = helper(index + 1, total ^ nums[index])
        exclude = helper(index + 1, total)

        return include + exclude

    return helper(0, 0)