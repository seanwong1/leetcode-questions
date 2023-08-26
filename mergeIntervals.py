# Leetcode 56

from typing import *

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda pair: pair[0])
    newIntervals = []
    counter = 1
    if len(intervals) == 1:
      return intervals
    while counter <= len(intervals):
      if not len(newIntervals):
        start1, end1 = intervals[counter - 1]
      else:
        start1, end1 = newIntervals[-1]
      start2, end2 = intervals[counter]
      if end1 >= start2:
        newIntervals.append([min(start1, start2), max(end1, end2)])
        counter += 1
      else:
        newIntervals.append(intervals[counter - 1])
        if counter == len(intervals) - 1:
          newIntervals.append(intervals[counter])
      counter += 1
    return newIntervals

intervals = [[1,4],[0,2],[3,5]]
s = Solution()
print(s.merge(intervals))