# Leetcode 1365

from typing import List
from collections import Counter

class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    counter = Counter(nums)
    result = []

    for current in nums:
      result.append(sum([count for num, count in counter.items() if num < current]))

    return result