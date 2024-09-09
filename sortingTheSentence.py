# Leetcode 1859

class Solution:
  def sortSentence(self, s: str) -> str:
    s = s.split(' ')
    words = [None] * len(s)

    for word in s:
      words[int(word[-1]) - 1] = word[:-1]

    return ' '.join(words)