# Leetcode 455

from typing import List

class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    content = 0
    g.sort()
    s.sort()
    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
      if s[cookie] >= g[child]:
        content += 1
        child += 1
      cookie += 1

    return content