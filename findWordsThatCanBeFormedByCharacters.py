# Leetcode 1160

from typing import List
from collections import Counter

class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    result = 0
    charCount = Counter(chars)

    for word in words:
      wordCount = Counter(word)
      if wordCount <= charCount:
        result += len(word)

    return result