# Leetcode 647

class Solution:
  def countSubstrings(self, s: str) -> int:
    count = 0
    for i in range(len(s)):
      counter = 0
      while i - counter >= 0 and i + counter < len(s) and s[i - counter] == s[i + counter]:
        if s[i - counter] == s[i + counter]:
          count += 1
          counter += 1
      counter = 0
      while i - counter >= 0 and i + 1 + counter < len(s) and s[i - counter] == s[i + 1 + counter]:
        if s[i - counter] == s[i + 1 + counter]:
          count += 1
          counter += 1
    return count

s = Solution()
print(s.countSubstrings('aaa'))