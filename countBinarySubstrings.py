# Leetcode 696

class Solution:
  def countBinarySubstrings(self, s: str) -> int:
    count = 0
    current = 1
    same = 0

    for i in range(1, len(s)):
      if s[i] != s[i - 1]:
        same = current
        current = 1
      else:
        current += 1

      if same >= current:
        count += 1

    return count