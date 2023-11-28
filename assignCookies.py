# Leetcode 455

from typing import List

class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    child = 0

    for cookie in s:
      if cookie >= g[child]:
        child += 1
      if child > len(g) - 1:
        break

    return child