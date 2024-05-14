# Leetcode 1394

from typing import List
from collections import Counter

class Solution:
  def findLucky(self, arr: List[int]) -> int:
    counter = Counter(arr)
    result = -1

    for index, value in counter.items():
      if index == value and value > result:
        result = index

    return result