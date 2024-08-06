# Leetcode 1763

class Solution:
  def longestNiceSubstring(self, s: str) -> str:
    sSet = set(s)

    for i in range(len(s) - 1, -1, -1):
      if not s[i].swapcase() in sSet:
        right = self.longestNiceSubstring(s[i + 1:])
        left = self.longestNiceSubstring(s[:i])
        return right if len(right) > len(left) else left

    return s