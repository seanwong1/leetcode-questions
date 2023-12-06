# Leetcode 495

from typing import List

class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    result = 0

    for time in range(1, len(timeSeries)):
      if timeSeries[time] - timeSeries[time - 1] >= duration:
        result += duration
      else:
        result += timeSeries[time] - timeSeries[time - 1]

    return result