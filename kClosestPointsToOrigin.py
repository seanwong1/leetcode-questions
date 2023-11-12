# Leetcode 973

from typing import List

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    distances = {}
    result = []

    for point in points:
      distance = ((abs(point[0]) ** 2) + (abs(point[1]) ** 2)) ** (1 / 2)
      if not distance in distances:
        distances[distance] = [point]
      else:
        distances[distance].append(point)

    for i in sorted(distances.keys()):
      while k > 0 and len(distances[i]):
        result.append(distances[i].pop())
        k -= 1

      if k <= 0:
        break

    return result