# Leetcode 1869

class Solution:
  def checkZeroOnes(self, s: str) -> bool:
    ones = s.split('0')
    zeroes = s.split('1')
    return len(max(ones)) > len(max(zeroes))