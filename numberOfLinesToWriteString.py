# Leetcode 806

from typing import List

class Solution:
  def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    lines = 0
    width = 0

    for char in s:
      if width + widths[ord(char) - 97] > 100:
        lines += 1
        width = widths[ord(char) - 97]
      else:
        width += widths[ord(char) - 97]

    return (lines + 1, width)