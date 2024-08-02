# Leetcode 1748

from typing import List
from collections import Counter

class Solution:
  def sumOfUnique(self, nums: List[int]) -> int:
    counter = Counter(nums)
    result = 0

    for num, freq in counter.items():
      if freq == 1:
        result += num

    return result