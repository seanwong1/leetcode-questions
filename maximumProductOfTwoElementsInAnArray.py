# Leetcode 1464

from typing import List
from heapq import _heapify_max, _heappop_max

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    _heapify_max(nums)

    num1 = _heappop_max(nums)
    num2 = _heappop_max(nums)

    return (num1 - 1) * (num2 - 1)