# Leetcode 1725

from typing import List

class Solution:
  def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
    squares = []

    for rectangle in rectangles:
      squares.append(min(rectangle))

    return squares.count(max(squares))