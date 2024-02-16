# Leetcode 868

class Solution:
  def binaryGap(self, n: int) -> int:
    maxGap = 0
    bitN = bin(n).replace('0b', '')
    gap = '11'

    for i in range(len(bitN) - 1):
      if bitN.find(gap) != -1:
        maxGap = len(gap) - 1

      gap = gap[:-1] + '01'

    return maxGap