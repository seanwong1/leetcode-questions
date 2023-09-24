# Leetcode 528

from typing import List
from random import random

class Solution:
  def __init__(self, w: List[int]):
    self.w = []
    self.total = sum(w)
    cumulative = 0
    for weight in w:
      cumulative += weight
      self.w.append(cumulative / self.total)

  def pickIndex(self) -> int:
    num = random()
    for i in range(len(self.w)):
      if num <= self.w[i]:
        return i