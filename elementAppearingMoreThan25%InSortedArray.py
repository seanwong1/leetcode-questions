# Leetcode 1287

from typing import List
from collections import Counter

class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    counter = Counter(arr)

    return max(counter, key=counter.get)