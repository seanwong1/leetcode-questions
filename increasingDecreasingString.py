# Leetcode 1370

from collections import Counter

class Solution:
  def sortString(self, s: str) -> str:
    counter = Counter(s)
    result = ''
    current = 0

    while current < len(s):
      for i in range(26):
        if counter[chr(97 + i)] > 0:
          result += chr(97 + i)
          counter [chr(97 + i)] -= 1
          current += 1
      for i in range(25, -1, -1):
        if counter[chr(97 + i)] > 0:
          result += chr(97 + i)
          counter [chr(97 + i)] -= 1
          current += 1

    return result