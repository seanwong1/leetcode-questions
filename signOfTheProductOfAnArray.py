# Leetcode 1822

from typing import List

class Solution:
  def arraySign(self, nums: List[int]) -> int:
    product = nums[0]

    if product == 0:
      return 0

    for index, num in enumerate(nums[1:]):
      if num < 0:
        product *= -1
      elif num == 0:
        return 0

    return -1 if product < 0 else 1