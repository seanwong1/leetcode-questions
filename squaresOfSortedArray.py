# Leetcode 977

from typing import List

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    storage = []
    result = []

    for num in nums:
      if num < 0:
        storage.append(num)
      else:
        while storage and abs(storage[-1]) < num:
          result.append(storage.pop() ** 2)
        result.append(num ** 2)

    while storage:
      result.append(storage.pop() ** 2)

    return result