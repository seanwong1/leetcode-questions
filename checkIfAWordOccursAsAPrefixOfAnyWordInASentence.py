# Leetcode 1455

class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    result = -1
    words = sentence.split(' ')
    prefixLen = len(searchWord)

    for index, word in enumerate(words):
      if len(word) >= prefixLen and searchWord == word[:prefixLen]:
        result = index + 1
        break

    return result