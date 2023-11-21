# Leetcode 414

from typing import List

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    nums = sorted(nums)
    result = [nums.pop()]
    counter = 1

    while counter <= 2 and len(nums):
      largest = nums.pop()
      if result[-1] != largest:
        result.append(largest)
        counter += 1

    return result[-1] if len(result) > 2 else max(result)