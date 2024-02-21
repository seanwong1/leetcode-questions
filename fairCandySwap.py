# Leetcode 888

from typing import List

class Solution:
  def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    sumAlice = sum(aliceSizes)
    sumBob = sum(bobSizes)
    midpoint = (sumAlice + sumBob) // 2
    bobSet = set(bobSizes)

    for aliceBox in aliceSizes:
      bobBox = midpoint - sumAlice + aliceBox
      if bobBox in bobSet:
        return [aliceBox, bobBox]