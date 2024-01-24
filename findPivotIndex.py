# Leetcode 724

from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    leftCumulative = [nums[0]] * len(nums)
    rightCumulative = [nums[-1]] * len(nums)

    for i in range(1, len(nums)):
      leftCumulative[i] = leftCumulative[i - 1] + nums[i]

    for i in range(len(nums) - 2, -1, -1):
      rightCumulative[i] = rightCumulative[i + 1] + nums[i]

    for i in range(len(nums)):
      if leftCumulative[i] == rightCumulative[i]:
        return i

    return -1