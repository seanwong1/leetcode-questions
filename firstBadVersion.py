# Leetcode 278

# def isBadVersion(version: int) -> bool:

class Solution:
  def firstBadVersion(self, n: int) -> int:
    goodVersion = 1
    badVersion = n

    while goodVersion <= badVersion:
      midpoint = badVersion + (goodVersion - badVersion) // 2
      if isBadVersion(midpoint):
        badVersion = midpoint - 1
      else:
        goodVersion = midpoint + 1

    return badVersion