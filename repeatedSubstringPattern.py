# Leetcode 459

class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    return True if s in s * 2[1:-1] else False