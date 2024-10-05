# Leetcode 1909

from typing import List

class Solution:
  def canBeIncreasing(self, nums: List[int]) -> bool:
    counter = 0
    num = 0
    current = 1
    loop1 = True

    while num + current < len(nums):
      if nums[num] >= nums[num + current]:
        counter += 1
        current += 1
      else:
        num += current
        current = 1

      if counter > 1:
        loop1 = False

    counter = 0
    num = len(nums) - 1
    current = 1

    while num - current >= 0:
      if nums[num] <= nums[num - current]:
        counter += 1
        current += 1
      else:
        num -= current
        current = 1

      if counter > 1:
        return loop1

    return True