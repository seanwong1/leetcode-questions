# Leetcode 1588

from typing import List

class Solution:
  def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    length = len(arr)
    result = 0

    for i in range(length):
      factor = ((i + 1) * (length - i) + 1) // 2
      result += arr[i] * factor
      result += arr[length - i - 1] * factor

    return result