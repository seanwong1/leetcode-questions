# Leetcode 1925

import math

class Solution:
  def countTriples(self, n: int) -> int:
    count = 0

    for i in range(1, n):
      for j in range(i + 1, n):
        k = math.sqrt(i ** 2 + j ** 2)
        if k.is_integer() and k <= n:
          count += 1

    return count * 2