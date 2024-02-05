# Leetcode 812

from typing import List

class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    area = 0
    for i in range(len(points)):
      Ax, Ay = points[i]
      for j in range(i, len(points)):
        Bx, By = points[j]
        for k in range(j, len(points)):
          Cx, Cy = points[k]
          area = max(area, abs((Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By)) / 2))

    return area