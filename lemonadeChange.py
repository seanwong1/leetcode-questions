# Leetcode 860

from typing import List

class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    storage = {5: 0, 10: 0, 20: 0}

    for bill in bills:
      storage[bill] += 1
      if bill == 10:
        storage[5] -= 1
      elif bill == 20:
        if storage[10] > 0:
          storage[10] -= 1
          storage[5] -= 1
        else:
          storage[5] -= 3
      if storage[5] < 0 or storage[10] < 0:
        return False

    return True