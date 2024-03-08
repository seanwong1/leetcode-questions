# Leetcode 976

from typing import List
import heapq

class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    sides = [num * -1 for num in nums]
    heapq.heapify(sides)

    side1 = heapq.heappop(sides) * -1
    side2 = heapq.heappop(sides) * -1
    side3 = heapq.heappop(sides) * -1

    while sides:
      if self.isValidTriangle(side1, side2, side3):
        return side1 + side2 + side3
      else:
        side1 = side2
        side2 = side3
        side3 = heapq.heappop(sides) * -1

    return side1 + side2 + side3 if self.isValidTriangle(side1, side2, side3) else 0

  def isValidTriangle(self, a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
      return False
    else:
      return True