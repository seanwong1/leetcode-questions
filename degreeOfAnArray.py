# Leetcode 697

from typing import List

class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    storage = {}
    counts = {}
    result = 0
    degree = 0

    for i in range(len(nums)):
      if not nums[i] in counts:
        counts[nums[i]] = 1
        storage[nums[i]] = i
      else:
        counts[nums[i]] += 1

      if counts[nums[i]] > degree:
        degree = max(degree, counts[nums[i]])
        result = i - storage[nums[i]] + 1
      elif counts[nums[i]] == degree:
        result = min(result, i - storage[nums[i]] + 1)

    return result