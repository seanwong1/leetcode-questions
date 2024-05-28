# Leetcode 1486

class Solution:
  def xorOperation(self, n: int, start: int) -> int:
    result = 0

    for i in range(start, (2 * n) + start, 2):
      result ^= i

    return result