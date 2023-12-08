# Leetcode 500

from typing import List

class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    result = []
    rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

    for word in words:
      wordSet = set(word.lower())
      if wordSet.issubset(rows[0]) or wordSet.issubset(rows[1]) or wordSet.issubset(rows[2]):
        result.append(word)

    return result