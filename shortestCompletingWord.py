# Leetcode 748

from typing import List
from collections import Counter

class Solution:
  def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    storage = []

    chars = Counter([char.lower() for char in licensePlate if char.isalpha()])

    for word in words:
      wordCounter = Counter(word)
      if not chars - wordCounter:
        storage.append(word)

    return min(storage, key=len)