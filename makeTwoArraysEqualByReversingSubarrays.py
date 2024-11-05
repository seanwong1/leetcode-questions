# Leetcode 1460

from typing import List
from collections import Counter

class Solution:
  def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    counter = Counter(target)

    for index, num in enumerate(arr):
      if num in counter:
        counter[num] -= 1

    for key, value in counter.items():
      if value != 0:
        return False

    return True

    # return Counter(target) == Counter(arr)