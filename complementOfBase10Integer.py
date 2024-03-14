# Leetcode 1009

class Solution:
  def bitwiseComplement(self, n: int) -> int:
    return int(''.join(['0' if bit == '1' else '1' for bit in bin(n).replace('0b', '')]), 2)