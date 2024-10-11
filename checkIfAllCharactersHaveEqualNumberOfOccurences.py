# Leetcode 1941

from collections import Counter

class Solution:
  def areOccurrencesEqual(self, s: str) -> bool:
    counter = Counter(s)
    avg = len(s) / len(counter)

    if not avg.is_integer():
      return False

    avg = int(avg)

    for key, value in counter.items():
      if value != avg:
        return False

    return True