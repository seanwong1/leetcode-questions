# Leetcode 1637

from typing import List

class Solution:
  def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    widest = 0
    numLine = []

    for point in points:
      numLine.append(point[0])

    numLine.sort()

    for i in range(len(numLine) - 1):
      widest = max(widest, numLine[i + 1] - numLine[i])

    return widest