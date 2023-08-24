# Leetcode 5

class Solution:
  def longestPalindrome(self, s: str) -> str:
    length = 1
    palindrome = s[0]

    if s == s[::-1]:
      return s

    for i in range(len(s)):
      left = i
      right = i + 1
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      if len(s[left + 1:right]) > length:
        palindrome = s[left + 1:right]
        length = len(palindrome)
      left = i
      right = i
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      if len(s[left + 1:right]) > length:
        palindrome = s[left + 1:right]
        length = len(palindrome)
    return palindrome