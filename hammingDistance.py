# Leetcode 461

class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    return sum(int(bit) for bit in bin(x ^ y).replace('0b', ''))