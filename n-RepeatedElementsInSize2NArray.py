# Leetcode 961

from typing import List
from collections import Counter

class Solution:
  def repeatedNTimes(self, nums: List[int]) -> int:
    counts = Counter(nums)

    for count in counts:
      if counts[count] == len(nums) // 2:
        return count