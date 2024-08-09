# Leetcode 1779

from typing import List

class Solution:
  def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    result = -1
    prev_manhattan = -1

    for index, point in enumerate(points):
      x2, y2 = point

      if x2 == x or y2 == y:
        manhattan = abs(x - x2) + abs(y - y2)
        if result == -1:
          result = index
          prev_manhattan = manhattan
        elif manhattan < prev_manhattan:
          result = index
          prev_manhattan = manhattan

    return result