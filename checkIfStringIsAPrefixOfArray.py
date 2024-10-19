# Leetcode 1961

from typing import List

class Solution:
  def isPrefixString(self, s: str, words: List[str]) -> bool:
    for i in range(1, len(words) + 1):
      if ''.join(words[0:i]) == s:
        return True

    return False