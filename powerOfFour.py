# Leetcode 342

import math

class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    if n <= 0:
      return False

    return round(math.log(n, 4), 9).is_integer()