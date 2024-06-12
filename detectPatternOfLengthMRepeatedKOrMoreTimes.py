# Leetcode 1566

from typing import List

class Solution:
  def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    repeats = 1
    prev = tuple(arr[:m])
    count = 0

    while count + 2 * m <= len(arr):
      pattern = tuple(arr[m + count:count + 2 * m])

      if pattern == prev:
        repeats += 1
        if repeats >= k:
          return True
        count += m
      else:
        prev = tuple(arr[count + 1: count + 1 + m])
        repeats = 1
        count += 1

    return False