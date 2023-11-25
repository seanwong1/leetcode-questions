# Leetcode 448

from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    return list(set(range(1, len(nums) + 1)).difference(set(nums)))