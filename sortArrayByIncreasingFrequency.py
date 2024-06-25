# Leetcode 1636

from typing import List
from collections import Counter

class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    counter = Counter(nums)

    return sorted(nums, key=lambda x: [counter[x], -x])