# Leetcode 997

from typing import *

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    counts = {}
    if not trust and n == 1:
      return n
    for pair in trust:
      if not pair[0] in counts:
        counts[pair[0]] = [1, 0]
      else:
        counts[pair[0]][0] += 1
      if not pair[1] in counts:
        counts[pair[1]] = [0, 1]
      else:
        counts[pair[1]][1] += 1

    for person in counts:
      if counts[person][0] == 0:
        if counts[person][1] == n - 1:
          return person

    return -1


n = 1
trust = []
s = Solution()
print(s.findJudge(n, trust))