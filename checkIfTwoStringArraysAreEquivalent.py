# Leetcode 1662

from typing import List

class Solution:
  def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    string1 = ''
    string2 = ''

    for letter in word1:
      string1 += letter

    for letter in word2:
      string2 += letter

    return string1 == string2