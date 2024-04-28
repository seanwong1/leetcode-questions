# Leetcode 1331

from typing import List

class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    nums = sorted(set(arr))
    ranks = {}
    result = []

    for index, num in enumerate(nums):
      ranks[num] = index + 1

    for index, num in enumerate(arr):
      result.append(ranks[num])

    return result