# Leetcode 941

from typing import List

class Solution:
  def validMountainArray(self, arr: List[int]) -> bool:
    if len(arr) < 3:
      return False

    peak = arr.index(max(arr))

    if peak == 0 or peak == len(arr) - 1:
      return False

    left = peak
    right = peak

    while left - 1 >= 0:
      if arr[left - 1] >= arr[left]:
        return False
      else:
        left -= 1

    while right + 1 < len(arr):
      if arr[right] <= arr[right + 1]:
        return False
      else:
        right += 1

    return True