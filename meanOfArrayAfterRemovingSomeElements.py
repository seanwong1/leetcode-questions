# Leetcode 1619

from typing import List

class Solution:
  def trimMean(self, arr: List[int]) -> float:
    arr.sort()
    factor = len(arr) // 20

    trimmed = arr[factor:len(arr) - factor]
    return sum(trimmed) / len(trimmed)