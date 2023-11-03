# Leetcode 326

import math

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
      return False

    return round(math.log(n, 3), 9).is_integer()