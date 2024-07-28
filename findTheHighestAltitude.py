# Leetcode 1732

from typing import List

class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    result = 0
    current = 0

    for point in gain:
      current += point
      result = max(result, current)

    return result