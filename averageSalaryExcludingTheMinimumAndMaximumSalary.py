# Leetcode 1491

from typing import List

class Solution:
  def average(self, salary: List[int]) -> float:
    minimum = min(salary)
    maximum = max(salary)
    total = sum(salary) - minimum - maximum

    return total / (len(salary) - 2)