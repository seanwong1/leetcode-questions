# Leetcode 594

from typing import List

class Solution:
  def findLHS(self, nums: List[int]) -> int:
    result = 0
    counts = {}

    for num in nums:
      if not num in counts:
        counts[num] = 1
      else:
        counts[num] += 1

    for num in counts:
      if num + 1 in counts:
        result = max(result, counts[num] + counts[num + 1])

    return result