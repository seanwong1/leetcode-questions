# Leetcode 1710

from typing import List

class Solution:
  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    result = 0

    for numBoxes, numUnits in boxTypes:
      if numBoxes <= truckSize:
        result += numBoxes * numUnits
        truckSize -= numBoxes
      else:
        result += truckSize * numUnits
        break

    return result