# Leetcode 1528

from typing import List

class Solution:
  def restoreString(self, s: str, indices: List[int]) -> str:
    result = [None] * len(s)

    for index, char in enumerate(s):
      result[indices[index]]= char

    return ''.join(result)