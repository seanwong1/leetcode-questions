# Leetcode 1071

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)
    shorter = min(str1, str2, key=len)

    for i in range(min(len1, len2), 0, -1):
      if not len1 % i and not len2 % i:
        quotient1 = len1 // (i)
        quotient2 = len2 // (i)
        if shorter[:i] * quotient1 == str1 and shorter[:i] * quotient2 == str2:
          return shorter[:i]

    return ''