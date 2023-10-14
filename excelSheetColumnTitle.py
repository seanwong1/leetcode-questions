# Leetcode 168

from typing import Tuple

class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    title = []
    while columnNumber > 0:
      columnNumber, letter = self.toBase(columnNumber, 26)
      title.append(chr(letter + 64))
    return ''.join(reversed(title))

  def toBase(self, n: int, base: int) -> Tuple[int, int]:
    position, remainder = divmod(n, base)

    if remainder == 0:
      return position - 1, remainder + base

    return position, remainder