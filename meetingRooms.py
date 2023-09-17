# Leetcode 920

from typing import *

class Interval():
  def __init__(self, start, end):
    self.start = start
    self.end = end

class Solution:
  """
  @param intervals: an array of meeting time intervals
  @return: if a person could attend all meetings
  """
  def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    intervals.sort(key=lambda interval: interval.start)
    start, end = intervals[0].start, intervals[0].end

    for i in range(1, len(intervals)):
      start = intervals[i].start
      if end > start:
        return False
      else:
        end = intervals[i].end

    return True