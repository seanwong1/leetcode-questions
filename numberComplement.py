# Leetcode 476

class Solution:
  def findComplement(self, num: int) -> int:
    return int(''.join(['0' if bit == '1' else '1' for bit in bin(num).replace('0b', '')]), 2)