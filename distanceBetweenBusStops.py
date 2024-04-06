# Leetcode 1184

from typing import List

class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    total = sum(distance)
    forward = 0
    stops = len(distance)

    if destination < start:
      [destination, start] = [start, destination]

    for stop in range(destination - start):
      forward += distance[(start + stop) % stops]

    return min(forward, total - forward)