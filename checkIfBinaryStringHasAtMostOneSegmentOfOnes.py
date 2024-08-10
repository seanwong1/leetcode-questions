# Leetcode 1784

class Solution:
  def checkOnesSegment(self, s: str) -> bool:
    numOnes = s.count('1')
    return s.find(numOnes * '1') > -1