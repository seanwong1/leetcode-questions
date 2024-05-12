# Leetcode 1385

from typing import List
from bisect import bisect

class Solution:
  def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    counter = 0

    for num in arr1:
      index = bisect(arr2, num)
      if index == 0:
        closest = arr2[index]
      elif index == len(arr2):
        closest = arr2[-1]
      else:
        before = arr2[index - 1]
        after = arr2[index]
        closest = before if abs(num - after) > abs(num - before) else after
      if abs(num - closest) > d:
        counter += 1

    return counter