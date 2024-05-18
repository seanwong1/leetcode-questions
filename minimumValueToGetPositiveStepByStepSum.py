# Leetcode 1413

from typing import List

class Solution:
  def minStartValue(self, nums: List[int]) -> int:
    storage = [0]

    for num in nums:
      storage.append(storage[-1] + num)

    return abs(min(storage)) + 1