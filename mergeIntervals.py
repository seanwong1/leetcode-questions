# Leetcode 56

from typing import *

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda interval: interval[0])
    newIntervals = [intervals[0]]

    for interval in intervals:
      start1, end1 = interval
      start2, end2 = newIntervals[-1]

      if end2 >= start1:
        newIntervals[-1][1] = end1 if end1 > end2 else end2
      elif start1 > end2:
        newIntervals.append(interval)

    return newIntervals