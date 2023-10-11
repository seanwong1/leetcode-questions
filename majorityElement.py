# Leetcode 169

from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    counts = {}
    majority = len(nums) // 2

    for num in nums:
      if not num in counts:
        counts[num] = 1
      else:
        counts[num] += 1

    for num in counts:
      if counts[num] > majority:
        return num

    return None