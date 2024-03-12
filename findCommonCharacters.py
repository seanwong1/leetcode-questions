# Leetcode 1002

from typing import List
from collections import Counter

class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    counter = Counter(words[0])
    result = ''

    for i in range(1, len(words)):
      counter = counter & Counter(words[i])

    for key, value in counter.items():
      result += key * value

    return list(result)