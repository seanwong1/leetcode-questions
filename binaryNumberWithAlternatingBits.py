# Leetcode 693

class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    binary = bin(n).replace("0b", "")

    if len(binary) <= 1:
      return True

    for i in range(len(binary) - 1):
      if binary[i] == binary[i + 1]:
        return False

    return True