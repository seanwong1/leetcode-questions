# Leetcode 1304

from typing import List

class Solution:
  def sumZero(self, n: int) -> List[int]:
    result = []

    if n % 2 != 0:
      result.append(0)

    for num in range(1, (n // 2) + 1):
      result.append(num)
      result.append(-num)

    return result