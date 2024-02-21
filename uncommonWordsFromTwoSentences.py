# Leetcode 884

from typing import List
from collections import Counter

class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    result = []
    frequency1 = Counter(s1.split())
    frequency2 = Counter(s2.split())

    for word, frequency in frequency1.items():
      if frequency == 1 and not word in frequency2:
        result.append(word)

    for word, frequency in frequency2.items():
      if frequency == 1 and not word in frequency1:
        result.append(word)

    return result