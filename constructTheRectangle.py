# Leetcode 492

from typing import List
import math

class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    for width in range(math.floor(area ** (1 / 2)), 0, -1):
      if area % width == 0:
        return [area // width, width]