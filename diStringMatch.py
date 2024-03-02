# Leetcode 942

from typing import List

class Solution:
  def diStringMatch(self, s: str) -> List[int]:
    increasing = 0
    decreasing = len(s)
    perm = []

    for char in s:
      if char == 'I':
        perm.append(increasing)
        increasing += 1
      else:
        perm.append(decreasing)
        decreasing -= 1

    perm.append(increasing if s[-1] == 'I' else decreasing)
    return perm