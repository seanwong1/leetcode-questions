# Leetcode 1523

class Solution:
  def countOdds(self, low: int, high: int) -> int:
    if low > 0 and low % 2 == 1:
      low -= 1
    if high < 10**9 and high % 2 == 1:
      high += 1

    return (high - low) // 2