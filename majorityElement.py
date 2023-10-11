# Leetcode 169

from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    counts = {}

    for num in nums:
      if not num in counts:
        counts[num] = 1
      else:
        counts[num] += 1

    return max(counts, key=counts.get)