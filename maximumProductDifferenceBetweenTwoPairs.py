# Leetcode 1913

from typing import List
import math
import heapq

class Solution:
  def maxProductDifference(self, nums: List[int]) -> int:
    return math.prod(heapq.nlargest(2, nums)) - math.prod(heapq.nsmallest(2, nums))