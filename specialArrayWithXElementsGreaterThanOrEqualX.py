# Leetcode 1608

from typing import List
from collections import Counter

class Solution:
  def specialArray(self, nums: List[int]) -> int:
    counter = Counter(nums)
    numsGreater = len(nums)

    for num in range(0, len(nums) + 1):
      if numsGreater == num:
        return num
      elif numsGreater < num:
        return -1
      else:
        if num in counter:
          numsGreater -= counter[num]