# Leetcode 1408

from typing import List

class Solution:
  def stringMatching(self, words: List[str]) -> List[str]:
    result = []

    for word1 in words:
      for word2 in words:
        if word1 != word2 and word1 in word2:
          result.append(word1)
          break

    return result