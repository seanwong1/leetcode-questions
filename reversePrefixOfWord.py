# Leetcode 2000

class Solution:
  def reversePrefix(self, word: str, ch: str) -> str:
    found = word.find(ch)

    if found > 0:
      word = word[0:found + 1][::-1] + word[found + 1:]

    return word