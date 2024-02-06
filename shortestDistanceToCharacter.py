# Leetcode 821

from typing import List

class Solution:
  def shortestToChar(self, s: str, c: str) -> List[int]:
    storage = [None] * len(s)
    prevC = None
    nextC = s.find(c)

    for i in range(len(s)):
      if nextC < i and not nextC == -1:
        prevC = nextC
        nextC = s.find(c, nextC + 1)

      if prevC == None:
        storage[i] = abs(nextC - i)
      elif nextC == -1:
        storage[i] = abs(prevC - i)
      else:
        storage[i] = min(abs(prevC - i), abs(nextC - i))

    return storage