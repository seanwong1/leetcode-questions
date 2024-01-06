# Leetcode 643

from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    total = sum(nums[0:k])
    result = total / k

    for i in range(1, len(nums) - k + 1):
      total = total - nums[i - 1] + nums[i + k - 1]
      average = total / k
      if average > result:
        result = average

    return result