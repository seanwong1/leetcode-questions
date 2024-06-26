# Leetcode 1299

from typing import List

class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    maximum = arr[-1]
    arr[-1] = -1

    for i in range(len(arr) - 2, -1, -1):
      temp = arr[i]
      arr[i] = maximum
      maximum = max(temp, maximum)

    return arr