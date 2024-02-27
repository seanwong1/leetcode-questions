# Leetcode 914

from typing import List
from collections import Counter
from math import gcd

class Solution:
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    groups = Counter(deck)
    return gcd(*set(groups.values())) != 1