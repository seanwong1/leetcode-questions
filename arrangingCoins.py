# Leetcode 441

class Solution:
  def arrangeCoins(self, n: int) -> int:
    for num in range(1, n + 1):
      if num + (num ** 2) > n * 2:
        return num - 1

    return 1