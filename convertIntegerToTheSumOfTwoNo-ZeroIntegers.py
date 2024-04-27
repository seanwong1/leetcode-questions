# Leetcode 1317

from typing import List

class Solution:
  def getNoZeroIntegers(self, n: int) -> List[int]:
    for i in range(1, n):
      j = str(n - i)
      if not '0' in str(i) and not '0' in j:
        return [i, n - i]