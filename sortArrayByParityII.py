# Leetcode 922

from typing import List

class Solution:
  def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    evens = []
    odds = []
    result = [None] * len(nums)

    for num in nums:
      if num % 2 == 0:
        evens.append(num)
      else:
        odds.append(num)

    for i in range(len(result)):
      if i % 2 == 0:
        result[i] = evens.pop()
      else:
        result[i] = odds.pop()

    return result