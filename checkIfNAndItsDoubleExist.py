# Leetcode 1346

from typing import List
from collections import Counter

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    counter = Counter(arr)

    for num in arr:
      if num == 0 and counter[num * 2] >= 2:
        return True
      if counter[num * 2] and num != 0:
        return True

    return False