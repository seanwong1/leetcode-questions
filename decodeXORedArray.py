# Leetcode 1720

from typing import List

class Solution:
  def decode(self, encoded: List[int], first: int) -> List[int]:
    result = [0] * (len(encoded) + 1)
    result[0] = first

    for i in range(len(result) - 1):
      result[i + 1] = encoded[i] ^ result[i]

    return result