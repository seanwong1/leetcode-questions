# Leetcode 1893

from typing import List

class Solution:
  def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    for i in range(left, right + 1):
      for index, rangee in enumerate(ranges):
        start, end = rangee
        if start <= i and i <= end:
          break
        if index == len(ranges) - 1:
          return False

    return True