# Leetcode 973

from typing import List

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def distance(point: List[int]) -> float:
      x, y = point
      return (x ** 2 + y ** 2) ** (1 / 2)

    points.sort(key=distance)

    return points[:k]