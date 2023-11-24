# Leetcode 441

class Solution:
  def arrangeCoins(self, n: int) -> int:
    return int((2 ** (1 / 2)) * ((n + (1 / 8)) ** (1 / 2)) - .5)