# Leetcode 2022

from typing import List

class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    converted = []

    if m * n != len(original):
      return converted

    for i in range(m):
      row = []
      for j in range(n):
        row.append(original[(i * n) + j])
      converted.append(row)

    return converted