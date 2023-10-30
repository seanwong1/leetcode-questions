# Leetcode 283

from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    counter = 0

    for num in nums:
      if num != 0:
        nums[counter] = num
        counter += 1

    for i in range(1, len(nums) + 1 - counter):
      nums[-i] = 0