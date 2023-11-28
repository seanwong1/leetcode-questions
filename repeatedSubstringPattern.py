# Leetcode 459

class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    for i in range(1, (len(s) // 2) + 1):
      for j in range(2, (len(s) // i) + 1):
        if s[0:i] * j == s:
          return True
    return False