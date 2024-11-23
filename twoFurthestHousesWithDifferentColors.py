# Leetcode 2078

from typing import List

class Solution:
  def maxDistance(self, colors: List[int]) -> int:
    leftDiff = 0
    rightDiff = 0

    for i in range(1, len(colors)):
      if colors[i] != colors[0]:
        leftDiff = i

    for i in range(len(colors) - 2, -1, -1):
      if colors[i] != colors[len(colors) - 1]:
        rightDiff = len(colors) - 1 - i

    return max(leftDiff, rightDiff)