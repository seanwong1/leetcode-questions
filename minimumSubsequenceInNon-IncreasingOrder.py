# Leetcode 1403

from typing import List

class Solution:
  def minSubsequence(self, nums: List[int]) -> List[int]:
    nums.sort(reverse=True)
    rightTotal = sum(nums)
    leftTotal = 0

    for index, num in enumerate(nums):
      rightTotal -= num
      leftTotal += num
      if leftTotal > rightTotal:
        break

    return nums[:index + 1]