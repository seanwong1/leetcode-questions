# Leetcode 575

from typing import List

class Solution:
  def distributeCandies(self, candyType: List[int]) -> int:
    storage = {}
    n = len(candyType) // 2

    for candy in candyType:
      if candy in storage:
        storage[candy] += 1
      else:
        storage[candy] = 0

    return len(storage) if len(storage) < n else n