# Leetcode 1848

from typing import List

class Solution:
  def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    minimum = len(nums)

    for index, num in enumerate(nums):
      if num == target:
        minimum = min(minimum, abs(index - start))

    return minimum