# Leetcode 1005

from typing import List
from heapq import nsmallest

class Solution:
  def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    numSum1 = sum(nums)
    numSum2 = 0
    smallest = nsmallest(k, nums)

    for num in smallest:
      if num < 0:
        numSum2 = numSum1
        numSum1 += (-num * 2)
        k -= 1
      else:
        numSum1 += (-num * 2 * (k % 2))
        break

    if smallest[-1] < 0 and k % 2 == 1:
      numSum1 += (num * 2)

    return max(numSum1, numSum2)