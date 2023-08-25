# Leetcode 55

from typing import *

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    jumpTo = len(nums) - 1
    for jump in range(len(nums) - 2, -1, -1):
      if nums[jump] + jump >= jumpTo:
        jumpTo = jump
    return True if jumpTo == 0 else False

s = Solution()
nums = [2,3,1,0,4]
print(s.canJump(nums))