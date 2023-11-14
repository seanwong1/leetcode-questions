# Leetcode 392

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 1 and s in t or s == '':
      return True
    elif s[0] in t:
      return self.isSubsequence(s[1:], t[t.index(s[0]) + 1:])
    else:
      return False

s = Solution()
print(s.isSubsequence('', 'ahbgdc'))