# Leetcode 55

from typing import *

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    jumpTo = len(nums) - 1
    for jumpFrom in range(len(nums) - 2, -1, -1):
      if nums[jumpFrom] + jumpFrom >= jumpTo:
        jumpTo = jumpFrom
    return True if jumpTo == 0 else False