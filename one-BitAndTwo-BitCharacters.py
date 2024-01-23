# Leetcode 717

from typing import List

class Solution:
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    def helper(index=0):
      if index == len(bits) - 1:
        return True
      if index == len(bits):
        return False
      if not bits[index]:
        return helper(index + 1)
      else:
        return helper(index + 2)

    return helper()