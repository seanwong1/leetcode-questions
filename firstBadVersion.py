# Leetcode 278

# def isBadVersion(version: int) -> bool:

class Solution:
  def firstBadVersion(self, n: int) -> int:
    goodVersion = 0
    badVersion = n
    found = False

    while not found:
      midpoint = (badVersion + goodVersion + 1) // 2
      if isBadVersion(midpoint):
        badVersion = midpoint
      else:
        goodVersion = midpoint

      if goodVersion + 1 == badVersion:
        found = True

    return badVersion