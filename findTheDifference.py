# Leetcode 389

class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    sSort = sorted(s)
    tSort = sorted(t)

    for i in range(len(sSort)):
      if sSort[i] != tSort[i]:
        return tSort[i]

    return tSort[-1]