# Leetcode 492

from typing import List
import math

class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    result = []
    print(math.ceil(area ** (1 / 2)))
    for width in range(1, math.floor(area ** (1 / 2)) + 1):
      if area % width == 0:
        result = [area // width, width]

    return result