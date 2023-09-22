# Leetcode 14

from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    longestPrefix = strs[0]

    for i in range(1, len(strs)):
      prefix = ''
      letter = 0

      while letter < len(longestPrefix) and letter < len(strs[i]):
        if longestPrefix[letter] == strs[i][letter]:
          prefix += strs[i][letter]
          letter += 1
        else:
          break
      longestPrefix = prefix

    return longestPrefix