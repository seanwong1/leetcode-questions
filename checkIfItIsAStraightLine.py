# Leetcode 1232

from typing import List
import math

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    try:
      m = (coordinates[-1][1] - coordinates[0][1]) / (coordinates[-1][0] - coordinates[0][0])
    except ZeroDivisionError:
      m = math.inf

    for i in range(len(coordinates) - 1):
      x1, y1 = coordinates[i]
      x2, y2 = coordinates[i + 1]

      try:
        m1 = ((y2 - y1) / (x2 - x1))
      except ZeroDivisionError:
        m1 = math.inf

      if m1 != m:
        return False

    return True