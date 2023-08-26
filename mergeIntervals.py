# Leetcode 56

from typing import *

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda interval: interval[0])
    newIntervals = [intervals[0]]

    for interval in intervals:
      if newIntervals[-1][1] >= interval[0]:
        newIntervals[-1][1] = interval[1] if interval[1] > newIntervals[-1][1] else newIntervals[-1][1]
      elif interval[0] > newIntervals[-1][1]:
        newIntervals.append(interval)

    return newIntervals