# Leetcode 1935

class Solution:
  def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    count = 0
    words = text.split(' ')

    for word in words:

      if not any(i in brokenLetters for i in word):
        count += 1

    return count