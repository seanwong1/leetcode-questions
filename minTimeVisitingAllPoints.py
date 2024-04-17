# Leetcode 1266

from typing import List

class Solution:
  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    result = 0

    for i in range(len(points) - 1):
      result += max(abs(points[i + 1][1] - points[i][1]), abs(points[i + 1][0] - points[i][0]))

    return result