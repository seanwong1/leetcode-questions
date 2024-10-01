# Leetcode 1897

from typing import List
from collections import Counter

class Solution:
  def makeEqual(self, words: List[str]) -> bool:
    counter = Counter()

    for word in words:
      counter.update(word)

    for key, value in counter.items():
      if not value % len(words) == 0:
        return False

    return True