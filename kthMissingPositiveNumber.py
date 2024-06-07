# Leetcode 1539

from typing import List

class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
      midpoint = (left + right) // 2
      if arr[midpoint] - midpoint - 1 < k:
        left = midpoint + 1
      else:
        right = midpoint - 1

    if arr[midpoint] - midpoint > k:
      return k + midpoint
    return k + midpoint + 1