# Leetcode 1128

from typing import List
from collections import Counter
from math import comb

class Solution:
  def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    result = 0

    counter = Counter(tuple([min(domino), max(domino)]) for domino in dominoes)

    for key, value in counter.items():
      result += comb(value, 2)

    return result