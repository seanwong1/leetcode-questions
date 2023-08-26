# Leetcode 213

from typing import *

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    def helper(houses):
      oldMax = 0
      newMax = 0

      for i in range(len(houses)):
        temp = oldMax + houses[i] if oldMax + houses[i] > newMax else newMax
        oldMax = newMax
        newMax = temp

      return newMax

    lastHouse = helper(nums[1:])
    firstHouse = helper(nums[0:-1])
    return firstHouse if firstHouse >= lastHouse else lastHouse