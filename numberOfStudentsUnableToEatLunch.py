# Leetcode 1700

from typing import List
from collections import Counter

class Solution:
  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    counter = Counter(students)

    for sandwich in sandwiches:
      if sandwich == 0:
        if counter[0] > 0:
          counter[0] -= 1
        else:
          break
      else:
        if counter[1] > 0:
          counter[1] -= 1
        else:
          break

    return sum(counter.values())