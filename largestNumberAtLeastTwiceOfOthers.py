# Leetcode 747

from typing import List

class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
    largest = max(nums)
    index = nums.index(largest)

    for i in range(len(nums)):
      if i == index:
        continue
      elif largest < nums[i] * 2:
        return -1

    return index