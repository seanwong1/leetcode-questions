# Leetcode 414

from typing import List

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    numsSet = set(nums)
    numsSet = sorted(numsSet)

    return numsSet[-1] if len(numsSet) < 3 else numsSet[-3]