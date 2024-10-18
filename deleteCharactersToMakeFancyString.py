# Leetcode 1957

class Solution:
  def makeFancyString(self, s: str) -> str:
    if len(s) > 2:
      newString = s[0:2]
    else:
      return s

    for i in range(2, len(s)):
      if s[i] != newString[-1] or s[i] != newString[-2]:
        newString += s[i]

    return newString