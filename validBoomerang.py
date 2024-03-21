# Leetcode 1037

from typing import List

class Solution:
  def isBoomerang(self, points: List[List[int]]) -> bool:
    def getSlope(p1, p2):
      if p2[0] - p1[0] == 0:
        return float('inf')
      else:
        return ((p2[1] - p1[1]) / (p2[0] - p1[0]))

    m = getSlope(points[0], points[-1])
    m1 = getSlope(points[0], points[1])
    m2 = getSlope(points[1], points[-1])

    return m1 != m2 and m1 != m and m2 != m