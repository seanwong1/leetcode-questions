# Leetcode 680

class Solution:
  def validPalindrome(self, s: str) -> bool:
    if s == s[::-1]:
      return True

    left = 0
    right = len(s) - 1

    while left <= right:
      if s[left] != s[right]:
        string1 = s[:left] + s[left + 1:]
        string2 = s[:right] + s[right + 1:]

        return string1 == string1[::-1] or string2 == string2[::-1]

      left += 1
      right -= 1

    return True