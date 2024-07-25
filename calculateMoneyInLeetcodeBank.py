# Leetcode 1716

from math import ceil

class Solution:
  def totalMoney(self, n: int) -> int:
    rows = ceil(n / 7)
    diff = rows * 7 - n

    return int(28 * rows + (7 * ((rows - 1) * rows) / 2) - ((diff) * (14 + 2 * rows - diff - 1) / 2))