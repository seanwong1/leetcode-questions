# Leetcode 303

from typing import List

class NumArray:
  def __init__(self, nums: List[int]):
    self.cumulative = [0]
    for i in range(len(nums)):
      self.cumulative.append(self.cumulative[i] + nums[i])

  def sumRange(self, left: int, right: int) -> int:
    return self.cumulative[right + 1] - self.cumulative[left]