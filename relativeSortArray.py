# Leetcode 1122

from typing import List
from collections import Counter

class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    counts = Counter(arr1)
    result = []

    for element in arr2:
      while counts[element] > 0:
        result.append(element)
        counts[element] -= 1
      del counts[element]

    rest = sorted(counts.keys())
    for element in rest:
      while counts[element] > 0:
        result.append(element)
        counts[element] -= 1

    return result