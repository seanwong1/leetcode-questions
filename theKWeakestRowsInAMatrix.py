# Leetcode 1337

from typing import List

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    rows = []

    for index, row in enumerate(mat):
      rows.append([index, sum(row)])

    rows.sort(key=lambda row:row[1])

    return [index for index, soldiers in rows[:k]]