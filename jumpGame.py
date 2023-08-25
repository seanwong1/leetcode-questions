# Leetcode 55

from typing import *

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
      return True
    else:
      for jump in range(len(nums) - 1):
        if nums[jump] + jump >= len(nums) - 1:
          return self.canJump(nums[0:jump + 1])
      return False

s = Solution()
nums = [2,3,1,0,4]
print(s.canJump(nums))