# Leetcode 509

class Solution:
  def fib(self, n: int) -> int:
    phi = (1 + 5 ** 0.5) / 2
    return int(((phi ** n) - (-1 / phi) ** n) / 5 ** (1 / 2))