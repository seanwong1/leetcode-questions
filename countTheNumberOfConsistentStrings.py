# Leetcode 1684

from typing import List

class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    allowed = set(allowed)
    inconsistent = 0

    for word in words:
      for letter in word:
        if not letter in allowed:
          inconsistent += 1
          break

    return len(words) - inconsistent