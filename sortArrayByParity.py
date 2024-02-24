# Leetcode 905

from typing import List

class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    sortedNums = [None] * len(nums)
    positive = 0
    negative = len(nums) - 1

    for num in nums:
      if num % 2 == 0:
        sortedNums[positive] = num
        positive += 1
      else:
        sortedNums[negative] = num
        negative -= 1

    return sortedNums