# Leetcode 1502

from typing import List

class Solution:
  def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    diff = (arr[-1] - arr[0]) / (len(arr) - 1)

    for i in range(len(arr) - 1):
      if arr[i + 1] - arr[i] != diff:
        return False

    return True