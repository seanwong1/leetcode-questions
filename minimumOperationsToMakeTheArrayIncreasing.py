# Leetcode 1827

from typing import List

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    operations = 0

    for index in range(len(nums) - 1):
      if nums[index + 1] <= nums[index]:
        operations += nums[index] + 1 - nums[index + 1]
        nums[index + 1] = nums[index] + 1

    return operations