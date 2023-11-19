# Leetcode 409

class Solution:
  def longestPalindrome(self, s: str) -> int:
    storage = {}
    result = 0
    hasOdd = 0

    for char in s:
      if char in storage:
        storage[char] += 1
      else:
        storage[char] = 1

    for value in storage.values():
      if value % 2 == 1:
        hasOdd = 1
        result += value - 1
      else:
        result += value

    return result + hasOdd